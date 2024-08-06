import pandas as pd
import json

#########################################document  
    
# user_video
df = pd.read_csv('../../generator/result/document/user_video.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['seq'] = eval(item['seq'])
with open('../transform_data/json_row/document/user_video.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
   
    
# video
df = pd.read_csv('../../generator/result/document/video.csv', encoding='utf-8')
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['video_id'] = item.pop('video_id')
    item['start'] = eval(item['start'])
    item['end'] = eval(item['end'])
    item['text'] = eval(item['text'])
with open('../transform_data/json_row/document/video.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
#########################################kv
# course_field
df = pd.read_csv('../../generator/result/kv/course_field.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['field_list'] = eval(item['field_list'])
with open('../transform_data/json_row/kv/course_field.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_course
df = pd.read_csv('../../generator/result/kv/user_course.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['course'] = eval(item['course'])
with open('../transform_data/json_row/kv/user_course.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
    
# user_problem
df = pd.read_csv('../../generator/result/kv/user_problem.csv', encoding='utf-8', sep="|")
json_data = df.to_json(orient='records', force_ascii=False)
data = json.loads(json_data)
for item in data:
    item['problem'] = eval(item['problem'])
with open('../transform_data/json_row/kv/user_problem.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)