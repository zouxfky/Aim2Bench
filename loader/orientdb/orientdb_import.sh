#!/bin/sh

start_time="$(date -u +%s)"

## Relational
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/relation/load_comment.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/relation/load_reply.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/relation/load_teacher.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/relation/load_user.json

end_time1="$(date -u +%s)"
elapsed1="$(($end_time1-$start_time))"
echo "The importing time for Relation data is $elapsed1" >> orientDBImportingtime


## Document
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/document/load_concept.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/document/load_course.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/document/load_problem.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/document/load_video.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/document/load_watched.json

end_time2="$(date -u +%s)"
elapsed2="$(($end_time2-$end_time1))"
echo "The importing time for JSON data is $elapsed2" >> orientDBImportingtime

## Graph
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_comment_involve_concept.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_comment_reply.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_comment_status.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_concept_prerequisites.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_course_commented.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_course_contain_concept.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_problem_contain_concept.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_reply_status.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_taughtby.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/graph/load_video_contain_concept.json

end_time3="$(date -u +%s)"
elapsed3="$(($end_time3-$end_time2))"
echo "The importing time for Graph data is $elapsed3" >> orientDBImportingtime

## kv
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/kv/load_course_selection.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/kv/load_field.json
sh /opt/orientdb/bin/oetl.sh /opt/Aim2Bench/loader/kv/load_record_problem.json

end_time4="$(date -u +%s)"
elapsed4="$(($end_time4-$end_time3))"
echo "The importing time for KV data is $elapsed4" >> orientDBImportingtime
