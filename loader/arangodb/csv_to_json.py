import pandas as pd
import json

#########################################document
# Concept
df = pd.read_csv('../../generator/result/document/concept.csv', encoding='utf-8')
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('concept_id')
    item['context'] = eval(item['context'])
with open('../transform_data/json/document/concept.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# Course
df = pd.read_csv('../../generator/result/document/course.csv', encoding='utf-8')
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('course_id')
    item['resource'] = eval(item['resource'])
with open('../transform_data/json/document/course.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# Problem
df = pd.read_csv('../../generator/result/document/problem.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('problem_id')
    item['answer'] = eval(item['answer'])
with open('../transform_data/json/document/problem.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_video
df = pd.read_csv('../../generator/result/document/user_video.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['seq'] = eval(item['seq'])
with open('../transform_data/json/document/user_video.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
   
    
# video
df = pd.read_csv('../../generator/result/document/video.csv', encoding='utf-8')
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('video_id')
    item['start'] = eval(item['start'])
    item['end'] = eval(item['end'])
    item['text'] = eval(item['text'])
with open('../transform_data/json/document/video.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
#########################################kv
# course_field
df = pd.read_csv('../../generator/result/kv/course_field.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['field_list'] = eval(item['field_list'])
with open('../transform_data/json/kv/course_field.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_course
df = pd.read_csv('../../generator/result/kv/user_course.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['course'] = eval(item['course'])
with open('../transform_data/json/kv/user_course.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_problem
df = pd.read_csv('../../generator/result/kv/user_problem.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['problem'] = eval(item['problem'])
with open('../transform_data/json/kv/user_problem.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
#########################################relation
# comment
df = pd.read_csv('../../generator/result/relation/comment.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('comment_id')
with open('../transform_data/json/relation/comment.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# reply
df = pd.read_csv('../../generator/result/relation/reply.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('reply_id')
with open('../transform_data/json/relation/reply.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
 

# teacher
df = pd.read_csv('../../generator/result/relation/teacher.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('teacher_id')
with open('../transform_data/json/relation/teacher.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
      
# user
df = pd.read_csv('../../generator/result/relation/user.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_key'] = item.pop('user_id')
with open('../transform_data/json/relation/user.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    

#########################################graph
# comment_concept
df = pd.read_csv('../../generator/result/graph/comment_concept.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('comment_id')
    item['_to'] = item.pop('concept_id')
with open('../transform_data/json/graph/comment_concept.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# comment_reply
df = pd.read_csv('../../generator/result/graph/comment_reply.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('comment_id')
    item['_to'] = item.pop('reply_id')
with open('../transform_data/json/graph/comment_reply.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# concept_prerequisites
df = pd.read_csv('../../generator/result/graph/concept_prerequisites.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('start_id')
    item['_to'] = item.pop('end_id')
with open('../transform_data/json/graph/concept_prerequisites.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# course_comment
df = pd.read_csv('../../generator/result/graph/course_comment.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('course_id')
    item['_to'] = item.pop('comment_id')
with open('../transform_data/json/graph/course_comment.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# course_concept
df = pd.read_csv('../../generator/result/graph/course_concept.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('course_id')
    item['_to'] = item.pop('concept_id')
with open('../transform_data/json/graph/course_concept.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# course_teacher
df = pd.read_csv('../../generator/result/graph/course_teacher.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('course_id')
    item['_to'] = item.pop('teacher_id')
with open('../transform_data/json/graph/course_teacher.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# problem_concept
df = pd.read_csv('../../generator/result/graph/problem_concept.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('problem_id')
    item['_to'] = item.pop('concept_id')
with open('../transform_data/json/graph/problem_concept.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_comment
df = pd.read_csv('../../generator/result/graph/user_comment.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('user_id')
    item['_to'] = item.pop('comment_id')
with open('../transform_data/json/graph/user_comment.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_reply
df = pd.read_csv('../../generator/result/graph/user_reply.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('user_id')
    item['_to'] = item.pop('reply_id')
with open('../transform_data/json/graph/user_reply.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# video_concept
df = pd.read_csv('../../generator/result/graph/video_concept.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['_from'] = item.pop('video_id')
    item['_to'] = item.pop('concept_id')
with open('../transform_data/json/graph/video_concept.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
