import psycopg2 
import time
host = "127.0.0.1"
port="5433"
dbname="Aim2Bench"
user="postgres"
password="123456"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)

with conn.cursor() as cursor:
    try :
        # 记录开始时间
        time_start = time.time()
        print('开始时间：',time_start)
        
        cursor.execute("""
        CREATE GRAPH benchmark;
        SET graph_path = benchmark;
        """)

        # Document
        cursor.execute(f"""

        LOAD FROM Concept AS source CREATE (n:Concept=to_jsonb(source));

        LOAD FROM Course AS source CREATE (n:Concept=to_jsonb(source));

        LOAD FROM Problem AS source CREATE (n:Concept=to_jsonb(source));

        CREATE TABLE temp(data jsonb);
        COPY temp (data) FROM '../transform_data/json_row/document/user_video.jsonl';
        INSERT INTO Watched (user_id, seq)
        SELECT data->>'user_id' AS user_id,
            jsonb_agg(seq) AS seq
        FROM temp,
            jsonb_array_elements(data->'seq') AS seq
        GROUP BY user_id;
        DROP TABLE temp;

        CREATE TABLE temp(data jsonb);
        COPY temp (data) FROM '../transform_data/json_row/document/video.jsonl';
        INSERT INTO Video (video_id, name, start, end1, text)
        SELECT data->>'video_id' AS video_id,
            data->>'name' AS name,
            jsonb_agg(start) AS start,
            jsonb_agg(end) AS end1,
            jsonb_agg(text) AS text
        FROM temp,
            jsonb_array_elements(data->'start') AS start,
            jsonb_array_elements(data->'end') AS end,
            jsonb_array_elements(data->'text') AS text
        GROUP BY video_id;
        DROP TABLE temp;
        LOAD FROM Video AS source CREATE (n:Video=to_jsonb(source)); 
        """)


        #  KV
        cursor.execute("""
        CREATE TABLE temp(data jsonb);
        COPY temp (data) FROM '../transform_data/json_row/kv/course_field.jsonl';
        INSERT INTO Field (course_id, field_list)
        SELECT data->>'course_id' AS course_id,
            jsonb_agg(field_list) AS field_list
        FROM temp,
            jsonb_array_elements(data->'field_list') AS field_list
        GROUP BY course_id;
        DROP TABLE temp;

        CREATE TABLE temp(data jsonb);
        COPY temp (data) FROM '../transform_data/json_row/kv/user_course.jsonl';
        INSERT INTO Course_selection (user_id, course)
        SELECT data->>'user_id' AS user_id,
            jsonb_agg(course) AS course
        FROM temp,
            jsonb_array_elements(data->'course') AS course
        GROUP BY user_id;
        DROP TABLE temp;

        CREATE TABLE temp(data jsonb);
        COPY temp (data) FROM '../transform_data/json_row/kv/user_problem_row.json';
        INSERT INTO Record_problem (user_id, problem)
        SELECT data->>'user_id' AS user_id,
            jsonb_agg(problem) AS problem
        FROM temp,
            jsonb_array_elements(data->'problem') AS problem
        GROUP BY user_id;
        DROP TABLE temp;
        """)

        #  Relation
        cursor.execute("""
        LOAD FROM Comment AS source CREATE (n:Comment=to_jsonb(source));
        LOAD FROM Reply AS source CREATE (n:Reply=to_jsonb(source));
        LOAD FROM Teacher AS source CREATE (n:Teacher=to_jsonb(source));
        LOAD FROM Users AS source CREATE (n:Users=to_jsonb(source)); 
        """)

        #  Graph
        cursor.execute("""
        LOAD FROM Comment_involve_concept AS source
        MATCH (n:Comment), (m:Concept)
        WHERE n.comment_id = to_jsonb((source).comment_id) AND m.concept_id = to_jsonb((source).concept_id)
        CREATE (n)-[r:Comment_involve_concept]->(m);

        LOAD FROM Comment_reply AS source
        MATCH (n:Comment), (m:Reply)
        WHERE n.comment_id = to_jsonb((source).comment_id) AND m.reply_id = to_jsonb((source).reply_id)
        CREATE (n)-[r:Comment_reply]->(m);
        
        LOAD FROM concept_prerequisites AS source
        MATCH (n:Concept), (m:Concept)
        WHERE n.concept_id = to_jsonb((source).start_id) AND m.concept_id = to_jsonb((source).end_id)
        CREATE (n)-[r:concept_prerequisites]->(m);

        LOAD FROM Course_commented AS source
        MATCH (n:Course), (m:Comment)
        WHERE n.course_id = to_jsonb((source).course_id) AND m.comment_id = to_jsonb((source).comment_id)
        CREATE (n)-[r:Course_commented]->(m);

        LOAD FROM Course_contain_concept AS source
        MATCH (n:Course), (m:Concept)
        WHERE n.course_id = to_jsonb((source).course_id) AND m.concept_id = to_jsonb((source).concept_id)
        CREATE (n)-[r:Course_contain_concept]->(m);
        
        LOAD FROM Taughtby AS source
        MATCH (n:Course), (m:Teacher)
        WHERE n.course_id = to_jsonb((source).course_id) AND m.teacher_id = to_jsonb((source).teacher_id)
        CREATE (n)-[r:Taughtby]->(m);
        
        LOAD FROM Problem_contain_concept AS source
        MATCH (n:Problem), (m:Concept)
        WHERE n.problem_id = to_jsonb((source).problem_id) AND m.concept_id = to_jsonb((source).concept_id)
        CREATE (n)-[r:Problem_contain_concept]->(m);
        
        LOAD FROM Comment_status AS source
        MATCH (n:User), (m:Comment)
        WHERE n.user_id = to_jsonb((source).user_id) AND m.comment_id = to_jsonb((source).comment_id)
        CREATE (n)-[r:Comment_status]->(m);
        
        LOAD FROM Reply_status AS source
        MATCH (n:User), (m:Reply)
        WHERE n.user_id = to_jsonb((source).user_id) AND m.reply_id = to_jsonb((source).reply_id)
        CREATE (n)-[r:Reply_status]->(m);
        
        LOAD FROM Video_contain_concept AS source
        MATCH (n:Video), (m:Concept)
        WHERE n.video_id = to_jsonb((source).video_id) AND m.concept_id = to_jsonb((source).concept_id)
        CREATE (n)-[r:Video_contain_concept]->(m);
        """)
        # 提交事务
        conn.commit()
        
        # 记录关闭时间
        time_end = time.time()
        print('结束时间：',time_end)

        # 程序执行时间
        time_sum = time_end - time_start
        print('导入用时：',time_sum)
        
    except Exception as ex:
        # 输出异常
        print(type(ex), ex)
        
        # 回滚
        conn.rollback()

