# -*- coding: utf-8 -*-
import json
import os
import pandas as pd
import datagen.dataGen as dataGen
import argparse
import sys

SCALE = {"comment": 4, "concept": 1165.5795, "course": 6.9122, "problem": 4487.0303, "reply": 4,
         "teacher": 8.9122, "user": 1, "video": 108.9232}
resources = ['concept', 'course', 'problem', 'school', 'teacher', 'video', 'course_teacher', 'course_school',
             'course_field', 'concept_course', 'concept_problem', 'concept_video', 'concept_prerequisites']
RADIX = 547
ratio = 0.05
RESULT_PATH = "result"
RELATION_PATH = "/relation"
DOCUMENT_PATH = "/document"
KV_PATH = "/kv"
GRAPH_PATH = "/graph"

COMMENT_ROW_FILENAME = "row_data/comment.csv"
COMMENT_RESULT_FILENAME = RESULT_PATH + RELATION_PATH + "/comment.csv"
CONCEPT_ROW_FILENAME = "row_data/concept.csv"
CONCEPT_RESULT_FILENAME = RESULT_PATH + DOCUMENT_PATH + "/concept.csv"
COURSE_ROW_FILENAME = "row_data/course.csv"
COURSE_RESULT_FILENAME = RESULT_PATH + DOCUMENT_PATH + "/course.csv"
PROBLEM_ROW_FILENAME = "row_data/problem.csv"
PROBLEM_RESULT_FILENAME = RESULT_PATH + DOCUMENT_PATH + "/problem.csv"
REPLY_ROW_FILENAME = "row_data/reply.csv"
REPLY_RESULT_FILENAME = RESULT_PATH + RELATION_PATH + "/reply.csv"
SCHOOL_ROW_FILENAME = "row_data/school.csv"
TEACHER_ROW_FILENAME = "row_data/teacher.csv"
TEACHER_RESULT_FILENAME = RESULT_PATH + RELATION_PATH + "/teacher.csv"
USER_RESULT_FILENAME = RESULT_PATH + RELATION_PATH + "/user.csv"
VIDEO_ROW_FILENAME = "row_data/video.csv"
VIDEO_RESULT_FILENAME = RESULT_PATH + DOCUMENT_PATH + "/video.csv"
FIELD_ROW_FILENAME = "row_data/field.csv"
COURSE_TEACHER_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/course_teacher.csv"
COURSE_FIELD_RESULT_FILENAME = RESULT_PATH + KV_PATH + "/course_field.csv"
COURSE_COMMENT_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/course_comment.csv"
USER_COURSE_RESULT_FILENAME = RESULT_PATH + KV_PATH + "/user_course.csv"
USER_PROBLEM_RESULT_FILENAME = RESULT_PATH + KV_PATH + "/user_problem.csv"
USER_VIDEO_RESULT_FILENAME = RESULT_PATH + DOCUMENT_PATH + "/user_video.csv"
USER_COMMENT_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/user_comment.csv"
USER_REPLY_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/user_reply.csv"
COMMENT_REPLY_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/comment_reply.csv"
COMMENT_CONCEPT_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/comment_concept.csv"
COURSE_CONCEPT_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/course_concept.csv"
PROBLEM_CONCEPT_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/problem_concept.csv"
VIDEO_CONCEPT_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/video_concept.csv"
CONCEPT_PREREQUISITES_RESULT_FILENAME = RESULT_PATH + GRAPH_PATH + "/concept_prerequisites.csv"

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser()
    parser.add_argument("--SF", help="规模因子", type=float)
    parser.add_argument("--config", help="JSON配置文件")
    # 解析命令行参数
    args = parser.parse_args()
    # 定义数据schema
    new_ratio = 0
    if args.SF is None and args.config is None:
        print("以 SF=0.1 规模生成数据！")
        new_ratio = ratio
    elif args.SF is not None and args.config is None:
        print("以 SF=%f 规模生成数据！" % args.SF)
        new_ratio = ratio * args.SF / 0.1
    else:
        with open(args.config) as f:
            config_file = json.load(f)
        if config_file.keys() != SCALE.keys():
            print("请参照example_config.file填写配置文件")
            sys.exit(0)
        for config_key, config_value in config_file.items():
            if not isinstance(config_value, int):
                print("请参照example_config.file填写配置文件")
                sys.exit(0)
            for everyKey in SCALE:
                if everyKey == config_key:
                    SCALE[everyKey] = config_value
        print("将参照配置文件生成数据！")
    if new_ratio != 0:
        for everyKey in SCALE:
            if everyKey in resources:
                SCALE[everyKey] = SCALE[everyKey] * RADIX * new_ratio
            else:
                SCALE[everyKey] = SCALE[everyKey] / SCALE["user"] * args.SF * 5000
    try:
        if not os.path.exists(RESULT_PATH):
            os.mkdir(RESULT_PATH)
        if not os.path.exists(RESULT_PATH + DOCUMENT_PATH):
            os.mkdir(RESULT_PATH + DOCUMENT_PATH)
        if not os.path.exists(RESULT_PATH + RELATION_PATH):
            os.mkdir(RESULT_PATH + RELATION_PATH)
        if not os.path.exists(RESULT_PATH + GRAPH_PATH):
            os.mkdir(RESULT_PATH + GRAPH_PATH)
        if not os.path.exists(RESULT_PATH + KV_PATH):
            os.mkdir(RESULT_PATH + KV_PATH)
    except BaseException as e:
        print(e)

    # print("--- start Generating Comment ---")
    # row_data = pd.read_csv(COMMENT_ROW_FILENAME)
    # dataGen.commentGen(COMMENT_RESULT_FILENAME, row_data, SCALE["comment"])
    # print("--- end Generating Comment ---\n\n")

    print("--- start Generating Concept ---")
    row_data = pd.read_csv(CONCEPT_ROW_FILENAME, delimiter='|')
    dataGen.conceptGen(CONCEPT_RESULT_FILENAME, row_data, SCALE["concept"])
    print("--- end Generating Concept ---\n\n")

    print("--- start Generating Course ---")
    row_data = pd.read_csv(COURSE_ROW_FILENAME, delimiter='|')
    dataGen.courseGen(COURSE_RESULT_FILENAME, row_data, SCALE["course"])
    print("--- end Generating Course ---\n\n")

    print("--- start Generating Problem ---")
    row_data = pd.read_csv(PROBLEM_ROW_FILENAME)
    dataGen.problemGen(PROBLEM_RESULT_FILENAME, row_data, SCALE["problem"])
    print("--- end Generating Problem ---\n\n")

    print("--- start Generating Reply ---")
    row_data = pd.read_csv(REPLY_ROW_FILENAME)
    dataGen.replyGen(REPLY_RESULT_FILENAME, row_data, SCALE["reply"])
    print("--- end Generating Reply ---\n\n")

    print("--- start Generating Teacher ---")
    row_data = pd.read_csv(TEACHER_ROW_FILENAME)
    dataGen.teacherGen(TEACHER_RESULT_FILENAME, row_data, SCALE["teacher"])
    print("--- end Generating Teacher ---\n\n")

    print("--- start Generating User ---")
    row_data = pd.read_csv(SCHOOL_ROW_FILENAME)
    dataGen.userGen(USER_RESULT_FILENAME, row_data, SCALE["user"])
    print("--- end Generating User ---\n\n")

    print("--- start Generating Video ---")
    row_data = pd.read_csv(VIDEO_ROW_FILENAME, delimiter='|')
    dataGen.videoGen(VIDEO_RESULT_FILENAME, row_data, SCALE["video"])
    print("--- end Generating Video ---\n\n")

    print("--- start Generating Course_Teacher ---")
    course = pd.read_csv(COURSE_RESULT_FILENAME, delimiter='|')
    teacher = pd.read_csv(TEACHER_RESULT_FILENAME, delimiter='|')
    dataGen.courseTeacherGen(COURSE_TEACHER_RESULT_FILENAME, course, teacher)
    print("--- end Generating Course_Teacher ---\n\n")

    print("--- start Generating Course_Field ---")
    course = pd.read_csv(COURSE_RESULT_FILENAME, delimiter='|')
    field = pd.read_csv(FIELD_ROW_FILENAME)
    dataGen.courseFiledGen(COURSE_FIELD_RESULT_FILENAME, course, field)
    print("--- end Generating Course_Field ---\n\n")

    print("--- start Generating Course_Comment ---")
    course = pd.read_csv(COURSE_RESULT_FILENAME, delimiter='|')
    comment = pd.read_csv(COMMENT_RESULT_FILENAME, delimiter='|')
    dataGen.courseCommentGen(COURSE_COMMENT_RESULT_FILENAME, course, comment)
    print("--- end Generating Course_Comment ---\n\n")

    print("--- start Generating User_Course ---")
    user = pd.read_csv(USER_RESULT_FILENAME, delimiter='|')
    course = pd.read_csv(COURSE_RESULT_FILENAME, delimiter='|')
    dataGen.userCourseGen(USER_COURSE_RESULT_FILENAME, user, course)
    print("--- end Generating User_Course ---\n\n")

    print("--- start Generating User_Problem ---")
    user = pd.read_csv(USER_RESULT_FILENAME, delimiter='|')
    problem = pd.read_csv(PROBLEM_RESULT_FILENAME, delimiter='|')
    dataGen.userProblemGen(USER_PROBLEM_RESULT_FILENAME, user, problem)
    print("--- end Generating User_Problem ---\n\n")

    print("--- start Generating User_Video ---")
    user = pd.read_csv(USER_RESULT_FILENAME, delimiter='|')
    video = pd.read_csv(VIDEO_RESULT_FILENAME, delimiter='|')
    dataGen.userVideoGen(USER_VIDEO_RESULT_FILENAME, user, video)
    print("--- end Generating User_Video ---\n\n")

    print("--- start Generating User_Comment ---")
    user = pd.read_csv(USER_RESULT_FILENAME, delimiter='|')
    comment = pd.read_csv(COMMENT_RESULT_FILENAME, delimiter='|')
    dataGen.userCommentGen(USER_COMMENT_RESULT_FILENAME, user, comment)
    print("--- end Generating User_Comment ---\n\n")

    print("--- start Generating User_Reply ---")
    user = pd.read_csv(USER_RESULT_FILENAME, delimiter='|')
    reply = pd.read_csv(REPLY_RESULT_FILENAME, delimiter='|')
    dataGen.userReplyGen(USER_REPLY_RESULT_FILENAME, user, reply)
    print("--- end Generating User_Reply ---\n\n")

    print("--- start Generating Comment_Reply ---")
    comment = pd.read_csv(COMMENT_RESULT_FILENAME, delimiter='|')
    reply = pd.read_csv(REPLY_RESULT_FILENAME, delimiter='|')
    dataGen.commentReplyGen(COMMENT_REPLY_RESULT_FILENAME, comment, reply)
    print("--- end Generating Comment_Reply ---\n\n")

    print("--- start Generating Comment_Concept ---")
    concept = pd.read_csv(CONCEPT_RESULT_FILENAME, delimiter='|')
    comment = pd.read_csv(COMMENT_RESULT_FILENAME, delimiter='|')
    dataGen.conceptCommentGen(COMMENT_CONCEPT_RESULT_FILENAME, concept, comment)
    print("--- end Generating Comment_Concept ---\n\n")

    print("--- start Generating Course_Concept ---")
    concept = pd.read_csv(CONCEPT_RESULT_FILENAME, delimiter='|')
    course = pd.read_csv(COURSE_RESULT_FILENAME, delimiter='|')
    dataGen.conceptCourseGen(COURSE_CONCEPT_RESULT_FILENAME, concept, course)
    print("--- end Generating Course_Concept ---\n\n")

    print("--- start Generating Problem_Concept ---")
    concept = pd.read_csv(CONCEPT_RESULT_FILENAME, delimiter='|')
    problem = pd.read_csv(PROBLEM_RESULT_FILENAME, delimiter='|')
    dataGen.conceptProblemGen(PROBLEM_CONCEPT_RESULT_FILENAME, concept, problem)
    print("--- end Generating Problem_Concept ---\n\n")

    print("--- start Generating Video_Concept ---")
    concept = pd.read_csv(CONCEPT_RESULT_FILENAME, delimiter='|')
    video = pd.read_csv(VIDEO_RESULT_FILENAME, delimiter='|')
    dataGen.conceptVideoGen(VIDEO_CONCEPT_RESULT_FILENAME, concept, video)
    print("--- end Generating Video_Concept ---\n\n")

    print("--- start Generating Concept_Prerequisite ---")
    concept = pd.read_csv(CONCEPT_RESULT_FILENAME, delimiter='|')
    dataGen.conceptPrerequisiteGen(CONCEPT_PREREQUISITES_RESULT_FILENAME, concept)
    print("--- end Generating Concept_Prerequisite ---\n\n")
