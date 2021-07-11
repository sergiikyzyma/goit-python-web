def query_find_all():
    return """SELECT id_exam, name_group,
                    student.last_name,
                    subject.name_subject,
                    teacher.last_name,teacher.grade,
                    punkts_by_subject,timepunkts_by_subject
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher;"""

def query_find_1():
    return """SELECT *
            FROM student;"""

def query_find_2():
    return """SELECT *
            FROM teacher;"""

def query_find_3():
    return """SELECT *
            FROM subject;"""
