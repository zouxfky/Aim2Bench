import psycopg2 
import age
import time
GRAPH_NAME = "benchmark"
host = "127.0.0.1"
port="5432"
dbname="Aim2Bench"
user="postgres"
password="123456"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
age.setUpAge(conn, GRAPH_NAME)

with conn.cursor() as cursor:
    try :
        # 记录开始时间
        time_start = time.time()
        print('开始时间：',time_start)
        
        # 加载age插件
        cursor.execute("""LOAD 'age';""", (GRAPH_NAME,) )
        cursor.execute("""SET search_path TO ag_catalog;""", (GRAPH_NAME,) )
        print('开始导入document')
        # 导入documentl文件
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Concept','../transform_data/add_id/document/concept.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Course','../transform_data/add_id/document/course.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Problem','../transform_data/add_id/document/problem.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Watched','../transform_data/add_id/document/user_video.csv', false);""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Video','../transform_data/add_id/document/video.csv');""", (GRAPH_NAME,) )
        print('开始导入kv')
        # 导入kv文件
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Field','../transform_data/add_id/kv/course_field.csv', false);""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Course_selection','../transform_data/add_id/kv/user_course.csv', false);""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Record_problem','../transform_data/add_id/kv/user_problem.csv', false);""", (GRAPH_NAME,) )
        print('开始导入relation')
        # 导入relation文件
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Comment','../transform_data/add_id/relation/comment.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Reply','../transform_data/add_id/relation/reply.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','Teacher','../transform_data/add_id/relation/teacher.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_labels_from_file('{GRAPH_NAME}','User','../transform_data/add_id/relation/user.csv');""", (GRAPH_NAME,) )
        print('开始导入graph')
        # 导入graph文件
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Comment_involve_concept','../transform_data/add_id/graph/comment_concept.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Comment_reply','../transform_data/add_id/graph/comment_reply.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Comment_status','../transform_data/add_id/graph/user_comment.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Course_commented','../transform_data/add_id/graph/course_comment.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Course_contain_concept','../transform_data/add_id/graph/course_concept.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Problem_contain_concept','../transform_data/add_id/graph/problem_concept.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Reply_status','../transform_data/add_id/graph/user_reply.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Taughtby','../transform_data/add_id/graph/course_teacher.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','Video_contain_concept','../transform_data/add_id/graph/video_concept.csv');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT load_edges_from_file('{GRAPH_NAME}','concept_prerequisites','../transform_data/add_id/graph/concept_prerequisites.csv');""", (GRAPH_NAME,) )

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

