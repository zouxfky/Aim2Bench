#!/bin/sh

python csv_to_json.py

sh json_to_jsonl.sh

start_time="$(date -u +%s)"

# document
arangoimp --file "/opt/benchmark/json/document/concept.jsonl" --type jsonl --collection "Concept" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/document/course.jsonl" --type jsonl --collection "Course" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/document/problem.jsonl" --type jsonl --collection "Problem" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/document/user_video.jsonl" --type jsonl --collection "Watched" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/document/video.jsonl" --type jsonl --collection "Video" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

end_time1="$(date -u +%s)"
elapsed1="$(($end_time1-$start_time))"
echo "The importing time for document data is $elapsed1" >> arangoDBImportingtime

# kv
arangoimp --file "/opt/benchmark/json/kv/course_field.jsonl" --type jsonl --collection "Field" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/kv/user_course.jsonl" --type jsonl --collection "Course_selection" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/kv/user_problem.jsonl" --type jsonl --collection "Record_problem" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

end_time2="$(date -u +%s)"
elapsed2="$(($end_time2-$end_time1))"
echo "The importing time for kv data is $elapsed2" >> arangoDBImportingtime

# relation
arangoimp --file "/opt/benchmark/json/relation/comment.jsonl" --type jsonl --collection "Comment" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/relation/reply.jsonl" --type jsonl --collection "Reply" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/relation/teacher.jsonl" --type jsonl --collection "Teacher" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/relation/user.jsonl" --type jsonl --collection "User" --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --threads 8  --server.database benchmark

end_time3="$(date -u +%s)"
elapsed3="$(($end_time3-$end_time2))"
echo "The importing time for relation data is $elapsed3" >> arangoDBImportingtime

# garph
arangoimp --file "/opt/benchmark/json/graph/comment_concept.jsonl" --type jsonl --collection "Comment_involve_concept" --from-collection-prefix Comment --to-collection-prefix Concept --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/comment_reply.jsonl" --type jsonl --collection "Comment_reply" --from-collection-prefix Comment --to-collection-prefix Reply --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/concept_prerequisites.jsonl" --type jsonl --collection "concept_prerequisites" --from-collection-prefix Concept --to-collection-prefix Concept --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/course_comment.jsonl" --type jsonl --collection "Course_commented" --from-collection-prefix Course --to-collection-prefix Comment --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/course_concept.jsonl" --type jsonl --collection "Course_contain_concept" --from-collection-prefix Course --to-collection-prefix Concept --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/course_teacher.jsonl" --type jsonl --collection "Taughtby" --from-collection-prefix Course --to-collection-prefix Teacher --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/problem_concept.jsonl" --type jsonl --collection "Problem_contain_concept" --from-collection-prefix Problem --to-collection-prefix Concept --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/user_comment.jsonl" --type jsonl --collection "Comment_status" --from-collection-prefix User --to-collection-prefix Comment --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/user_reply.jsonl" --type jsonl --collection "Reply_status" --from-collection-prefix User --to-collection-prefix Reply --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

arangoimp --file "/opt/benchmark/json/graph/video_concept.jsonl" --type jsonl --collection "Video_contain_concept" --from-collection-prefix Video --to-collection-prefix Concept --server.username root  --server.password "000000"  --server.endpoint tcp://192.168.157.235:8529  --create-collection true --create-collection-type edge --threads 8  --server.database benchmark

end_time4="$(date -u +%s)"
elapsed4="$(($end_time4-$end_time3))"
echo "The importing time for garph data is $elapsed4" >> arangoDBImportingtime
