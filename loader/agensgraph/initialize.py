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
        
        # 创建relation label
        cursor.execute(f"""
        
        create extension IF NOT EXISTS file_fdw;
        DROP SERVER import_server;
        CREATE SERVER import_server FOREIGN DATA WRAPPER file_fdw;

        DROP FOREIGN TABLE IF EXISTS Concept;
        DROP FOREIGN TABLE IF EXISTS Course;
        DROP FOREIGN TABLE IF EXISTS Problem;
        DROP FOREIGN TABLE IF EXISTS Watched;
        DROP FOREIGN TABLE IF EXISTS Video;

        DROP FOREIGN TABLE IF EXISTS Field;
        DROP FOREIGN TABLE IF EXISTS Course_selection;
        DROP FOREIGN TABLE IF EXISTS Record_problem;

        DROP FOREIGN TABLE IF EXISTS Comment;
        DROP FOREIGN TABLE IF EXISTS Reply;
        DROP FOREIGN TABLE IF EXISTS Teacher;
        DROP FOREIGN TABLE IF EXISTS Users;

        DROP FOREIGN TABLE IF EXISTS Comment_involve_concept;
        DROP FOREIGN TABLE IF EXISTS Comment_reply;
        DROP FOREIGN TABLE IF EXISTS concept_prerequisites;
        DROP FOREIGN TABLE IF EXISTS Course_commented;
        DROP FOREIGN TABLE IF EXISTS Course_contain_concept;
        DROP FOREIGN TABLE IF EXISTS Taughtby;
        DROP FOREIGN TABLE IF EXISTS Problem_contain_concept;
        DROP FOREIGN TABLE IF EXISTS Comment_status;
        DROP FOREIGN TABLE IF EXISTS Reply_status;
        DROP FOREIGN TABLE IF EXISTS Video_contain_concept;
        DROP GRAPH IF EXISTS benchmark cascade;



        create foreign table Concept(concept_id int8, concept_name varchar(255), context text)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/document/concept.csv');

        create foreign table Course(course_id int8, course_name varchar(255), prerequisites text, about text, resource text)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/document/course.csv');

        create foreign table Problem(problem_id int8, content text, option text, answer text, score float4, type int2, typetext varchar(255), language varchar(255))
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/document/problem.csv');

        create table IF NOT EXISTS Watched(user_id int8, seq JSONB);

        create table IF NOT EXISTS Video(video_id int8, name varchar(255), start JSONB, end1 JSONB, text JSONB);


        create table IF NOT EXISTS Field(course_id int8, field_list JSONB);

        create table IF NOT EXISTS Course_selection(user_id int8, course JSONB);

        create table IF NOT EXISTS Record_problem(user_id int8, problem JSONB);



        create foreign table Comment(comment_id int8, text text, create_time timestamp)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/relation/comment.csv');

        create foreign table Reply(reply_id int8, text text, create_time timestamp)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/relation/reply.csv');

        create foreign table Teacher(teacher_id int8, name varchar(20), about text, job_title varchar(255), org_name text)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/relation/teacher.csv');

        create foreign table Users(user_id int8, name varchar(20), gender varchar, school varchar(100), year_of_birth int2)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/relation/user.csv');


        create foreign table Comment_involve_concept(comment_id int8, concept_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/comment_concept.csv');

        create foreign table Comment_reply(comment_id int8, reply_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/comment_reply.csv');
        
        create foreign table concept_prerequisites(start_id int8, end_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/concept_prerequisites.csv');

        create foreign table Course_commented(course_id int8, comment_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/course_comment.csv');

        create foreign table Course_contain_concept(course_id int8, concept_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/course_concept.csv');
        
        create foreign table Taughtby(course_id int8, teacher_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/course_teacher.csv');
        
        create foreign table Problem_contain_concept(problem_id int8, concept_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/problem_concept.csv');
        
        create foreign table Comment_status(user_id int8, comment_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/user_comment.csv');
        
        create foreign table Reply_status(user_id int8, reply_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/user_reply.csv');
        
        create foreign table Video_contain_concept(video_id int8, concept_id int8)
        server import_server
        options(FORMAT 'csv', HEADER 'true', DELIMITER '|', NULL '', FILENAME '/opt/benchmark/result/graph/video_concept.csv');
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

