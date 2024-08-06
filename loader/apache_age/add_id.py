import pandas as pd
import json

#########################################document
print("开始转换document")
# Concept
df = pd.read_csv('../../generator/result/document/concept.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/document/concept.csv', index=False, encoding='utf-8', sep='|')

# Course
df = pd.read_csv('../../generator/result/document/course.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/document/course.csv', index=False, encoding='utf-8', sep='|')

# Problem
df = pd.read_csv('../../generator/result/document/problem.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/document/problem.csv', index=False, encoding='utf-8', sep='|')

# video
df = pd.read_csv('../../generator/result/document/video.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/document/video.csv', index=False, encoding='utf-8', sep='|')

#########################################relation


# comment
df = pd.read_csv('../../generator/result/relation/comment.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/relation/comment.csv', index=False, encoding='utf-8', sep='|')

# reply
df = pd.read_csv('../../generator/result/relation/reply.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/relation/reply.csv', index=False, encoding='utf-8', sep='|')

# teacher
df = pd.read_csv('../../generator/result/relation/teacher.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/relation/teacher.csv', index=False, encoding='utf-8', sep='|')

# user
df = pd.read_csv('../../generator/result/relation/user.csv', encoding='utf-8', sep='|')
first_column_values = df.iloc[:, 0]
df.insert(0, 'id', first_column_values)
df.to_csv('../transform_data/add_id/relation/user.csv', index=False, encoding='utf-8', sep='|')

#########################################graph
# comment_concept
df = pd.read_csv('../../generator/result/graph/comment_concept.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Comment')
df.insert(3, 'end_vertex_type', 'Concept')
df.to_csv('../transform_data/add_id/graph/comment_concept.csv', sep='|', index=False, encoding='utf-8')

# comment_reply
df = pd.read_csv('../../generator/result/graph/comment_reply.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Comment')
df.insert(3, 'end_vertex_type', 'Reply')
df.to_csv('../transform_data/add_id/graph/comment_reply.csv', sep='|', index=False, encoding='utf-8')

# concept_prerequisites
df = pd.read_csv('../../generator/result/graph/concept_prerequisites.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Concept')
df.insert(3, 'end_vertex_type', 'Concept')
df.to_csv('../transform_data/add_id/graph/concept_prerequisites.csv', sep='|', index=False, encoding='utf-8')

# course_comment
df = pd.read_csv('../../generator/result/graph/course_comment.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Course')
df.insert(3, 'end_vertex_type', 'Comment')
df.to_csv('../transform_data/add_id/graph/course_comment.csv', sep='|', index=False, encoding='utf-8')

# course_concept
df = pd.read_csv('../../generator/result/graph/course_concept.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Course')
df.insert(3, 'end_vertex_type', 'Concept')
df.to_csv('../transform_data/add_id/graph/course_concept.csv', sep='|', index=False, encoding='utf-8')

# course_teacher
df = pd.read_csv('../../generator/result/graph/course_teacher.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Course')
df.insert(3, 'end_vertex_type', 'Teacher')
df.to_csv('../transform_data/add_id/graph/course_teacher.csv', sep='|', index=False, encoding='utf-8')

# problem_concept
df = pd.read_csv('../../generator/result/graph/problem_concept.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Problem')
df.insert(3, 'end_vertex_type', 'Concept')
df.to_csv('../transform_data/add_id/graph/problem_concept.csv', sep='|', index=False, encoding='utf-8')

# user_comment
df = pd.read_csv('../../generator/result/graph/user_comment.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'User')
df.insert(3, 'end_vertex_type', 'Comment')
df.to_csv('../transform_data/add_id/graph/user_comment.csv', sep='|', index=False, encoding='utf-8')

# user_reply
df = pd.read_csv('../../generator/result/graph/user_reply.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'User')
df.insert(3, 'end_vertex_type', 'Reply')
df.to_csv('../transform_data/add_id/graph/user_reply.csv', sep='|', index=False, encoding='utf-8')

# video_concept
df = pd.read_csv('../../generator/result/graph/video_concept.csv', encoding='utf-8', sep="|")
df = df.rename(columns={df.columns[0]: 'start_id', df.columns[1]: 'end_id'})
df.insert(1, 'start_vertex_type', 'Video')
df.insert(3, 'end_vertex_type', 'Concept')
df.to_csv('../transform_data/add_id/graph/video_concept.csv', sep='|', index=False, encoding='utf-8')
