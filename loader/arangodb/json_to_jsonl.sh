# document
jq -c ".[]" ../transform_data/json/document/concept.json > ../transform_data/jsonl/document/concept.jsonl

jq -c ".[]" ../transform_data/json/document/course.json > ../transform_data/jsonl/document/course.jsonl

jq -c ".[]" ../transform_data/json/document/problem.json > ../transform_data/jsonl/document/problem.jsonl

jq -c ".[]" ../transform_data/json/document/user_video.json > ../transform_data/jsonl/document/user_video.jsonl

jq -c ".[]" ../transform_data/json/document/video.json > ../transform_data/jsonl/document/video.jsonl

# kv
jq -c ".[]" ../transform_data/json/kv/course_field.json > ../transform_data/jsonl/kv/course_field.jsonl

jq -c ".[]" ../transform_data/json/kv/user_course.json > ../transform_data/jsonl/kv/user_course.jsonl

jq -c ".[]" ../transform_data/json/kv/user_problem.json > ../transform_data/jsonl/kv/user_problem.jsonl

# relation
jq -c ".[]" ../transform_data/json/relation/comment.json > ../transform_data/jsonl/relation/comment.jsonl

jq -c ".[]" ../transform_data/json/relation/reply.json > ../transform_data/jsonl/relation/reply.jsonl

jq -c ".[]" ../transform_data/json/relation/teacher.json > ../transform_data/jsonl/relation/teacher.jsonl

jq -c ".[]" ../transform_data/json/relation/user.json > ../transform_data/jsonl/relation/user.jsonl

# garph
jq -c ".[]" ../transform_data/json/graph/comment_concept.json > ../transform_data/jsonl/graph/comment_concept.jsonl

jq -c ".[]" ../transform_data/json/graph/comment_reply.json > ../transform_data/jsonl/graph/comment_reply.jsonl

jq -c ".[]" ../transform_data/json/graph/concept_prerequisites.json > ../transform_data/jsonl/graph/concept_prerequisites.jsonl

jq -c ".[]" ../transform_data/json/graph/course_comment.json > ../transform_data/jsonl/graph/course_comment.jsonl

jq -c ".[]" ../transform_data/json/graph/course_concept.json > ../transform_data/jsonl/graph/course_concept.jsonl

jq -c ".[]" ../transform_data/json/graph/course_teacher.json > ../transform_data/jsonl/graph/course_teacher.jsonl

jq -c ".[]" ../transform_data/json/graph/problem_concept.json > ../transform_data/jsonl/graph/problem_concept.jsonl

jq -c ".[]" ../transform_data/json/graph/user_comment.json > ../transform_data/jsonl/graph/user_comment.jsonl

jq -c ".[]" ../transform_data/json/graph/user_reply.json > ../transform_data/jsonl/graph/user_reply.jsonl

jq -c ".[]" ../transform_data/json/graph/video_concept.json > ../transform_data/jsonl/graph/video_concept.jsonl
