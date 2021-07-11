def query_find_all():
    return """SELECT id_group, name_group,
                    student.fist_name,student.second_name,student.last_name,
                    subject.name_subject,
                    teacher.fist_name,teacher.second_name,teacher.last_name,
                    punkts_by_subject,timepunkts_by_subject
            FROM groups
            INNER JOIN student ON groups.id_student==student.id_student
            INNER JOIN subject ON groups.id_subject==subject.id_subject
            INNER JOIN teacher ON groups.id_teacher==teacher.id_teacher;"""

def query_find_1():
    return """SELECT *
            FROM student;"""

def query_find_2():
    return """SELECT *
            FROM teacher;"""

def query_find_3():
    return """SELECT *
            FROM subject;"""
