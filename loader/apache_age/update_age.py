import psycopg2 
import age
import time
import pandas as pd
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

        df = pd.read_csv('../transform_data/add_id/document/user_video.csv', sep='|')
        # 迭代每一行每一列的值
        for i, row in df.iterrows():
            columns_list = []
            value_list = []
            for column, value in row.items():
                columns_list.append(column)
                value_list.append(value)
            query = f'''
                        SELECT * FROM cypher('{GRAPH_NAME}', $$ 
                        MATCH (v: Watched{{user_id: '{value_list[0]}'}} ) 
                        SET v.{columns_list[1]} = {value_list[1]}
                        RETURN v 
                        $$) as (v agtype);
                        '''
            cursor.execute(query, (GRAPH_NAME,) ) 
            if i % 1000 == 0:
                print(i)  



        df = pd.read_csv('../transform_data/add_id/kv/course_field.csv', sep='|')
        # 迭代每一行每一列的值
        for i, row in df.iterrows():
            columns_list = []
            value_list = []
            for column, value in row.items():
                columns_list.append(column)
                value_list.append(value)
            query = f'''
                        SELECT * FROM cypher('{GRAPH_NAME}', $$ 
                        MATCH (v: Field{{course_id: '{value_list[0]}'}} ) 
                        SET v.{columns_list[1]} = {value_list[1]}
                        RETURN v 
                        $$) as (v agtype);
                        '''
            cursor.execute(query, (GRAPH_NAME,) ) 
            if i % 1000 == 0:
                print(i)     


        df = pd.read_csv('../transform_data/add_id/kv/user_course.csv', sep='|')
        # 迭代每一行每一列的值
        for i, row in df.iterrows():
            columns_list = []
            value_list = []
            for column, value in row.items():
                columns_list.append(column)
                value_list.append(value)
            query = f'''
                        SELECT * FROM cypher('{GRAPH_NAME}', $$ 
                        MATCH (v: Course_selection{{user_id: '{value_list[0]}'}} ) 
                        SET v.{columns_list[1]} = {value_list[1]}
                        RETURN v 
                        $$) as (v agtype);
                        '''
            cursor.execute(query, (GRAPH_NAME,) ) 
            if i % 1000 == 0:
                print(i) 


        df = pd.read_csv('../transform_data/add_id/kv/user_problem.csv', sep='|')
        # 迭代每一行每一列的值
        for i, row in df.iterrows():
            columns_list = []
            value_list = []
            for column, value in row.items():
                columns_list.append(column)
                value_list.append(value)
            query = f'''
                        SELECT * FROM cypher('{GRAPH_NAME}', $$ 
                        MATCH (v: Record_problem{{user_id: '{value_list[0]}'}} ) 
                        SET v.{columns_list[1]} = {value_list[1]}
                        RETURN v 
                        $$) as (v agtype);
                        '''
            cursor.execute(query, (GRAPH_NAME,) ) 
            if i % 1000 == 0:
                print(i)                                   

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

