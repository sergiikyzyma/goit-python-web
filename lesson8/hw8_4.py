import jinja2

def query_list_marks_all():
    return """SELECT id_exam, name_group,
                    student.last_name,
                    subject.name_subject,
                    teacher.last_name,teacher.grade,
                    punkts_by_subject,timepunkts_by_subject
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher;"""

def query_list_students():
    return """SELECT *
            FROM student;"""

def query_list_teachers():
    return """SELECT *
            FROM teacher;"""

def query_list_subjects():
    return """SELECT *
            FROM subject;"""

def query_list_students_in_group(name):
    result = jinja2.Template("""SELECT student.last_name,student.first_name,student.second_name,name_group
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            WHERE name_group = '{{name}}'
            ORDER BY student.last_name; """)
    return result.render(name=name)
