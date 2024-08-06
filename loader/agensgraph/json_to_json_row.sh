jq -c ".[]" ../transform_data/json_row/document/user_video.json > ../transform_data/json_row/document/user_video.jsonl
jq -c ".[]" ../transform_data/json_row/document/video.json > ../transform_data/json_row/document/video.jsonl
jq -c ".[]" ../transform_data/json_row/kv/course_field.json > ../transform_data/json_row/kv/course_field.jsonl
jq -c ".[]" ../transform_data/json_row/kv/user_course.json > ../transform_data/json_row/kv/user_course.jsonl
jq -c ".[]" ../transform_data/json_row/kv/user_problem.json > ../transform_data/json_row/kv/user_problem.jsonl