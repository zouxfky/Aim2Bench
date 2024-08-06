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

with conn.cursor() as cursor:
    cursor.execute("""LOAD 'age';""")
    cursor.execute("""SET search_path TO ag_catalog;""")
    cursor.execute(f"""SELECT create_graph('benchmark');""")
    conn.commit()

age.setUpAge(conn, GRAPH_NAME)
with conn.cursor() as cursor:
    try :
        # 记录开始时间
        time_start = time.time()
        print('开始时间：',time_start)
        
        # 加载age插件
        cursor.execute("""LOAD 'age';""", (GRAPH_NAME,) )
        cursor.execute("""SET search_path TO ag_catalog;""", (GRAPH_NAME,) )
        
        # 创建relation label
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Comment');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Reply');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Teacher');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','User');""", (GRAPH_NAME,) )

        # 创建document label
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Concept');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Course');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Problem');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Watched');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Video');""", (GRAPH_NAME,) )
        
        # 创建kv label
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Field');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Course_selection');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_vlabel('{GRAPH_NAME}','Record_problem');""", (GRAPH_NAME,) )

        # 创建graph label
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Course_contain_concept');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Comment_reply');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Comment_status');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Course_commented');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Comment_involve_concept');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Problem_contain_concept');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Reply_status');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Taughtby');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','Video_contain_concept');""", (GRAPH_NAME,) )
        cursor.execute(f"""SELECT create_elabel('{GRAPH_NAME}','concept_prerequisites');""", (GRAPH_NAME,) )
    
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

