import jinja2
from alembic import migration
#from alembic import op
from alembic.operations import ops
from sqlalchemy.orm import query
from hw9_2 import *                 # creating tables

def query_list_marks_all(session):
    return query.Query([Student, Teacher, Subject, Exam,], session).all()

def query_list_students(session):
    return query.Query([Student,], session).all()

def query_list_teachers(session):
    return query.Query([Teacher,], session).all()

def query_list_subjects(session):
    return query.Query([Subject,], session).all()

def query_find_1(id):
    result = jinja2.Template("""SELECT student,MAX(avg_mark),subject
            FROM (SELECT AVG(punkts_by_subject) as avg_mark,student.last_name as student,subject.name_subject as subject
                    FROM exam
                    INNER JOIN student ON exam.id_student==student.id_student
                    INNER JOIN subject ON exam.id_subject==subject.id_subject
                    WHERE subject.id_subject = {{id}}
                    GROUP BY student.last_name); """)
    return result.render(id=id)

def query_find_2(name):
    result = jinja2.Template("""SELECT student,MAX(avg_mark),subject
            FROM (SELECT AVG(punkts_by_subject) as avg_mark,student.last_name as student,subject.name_subject as subject
                    FROM exam
                    INNER JOIN student ON exam.id_student==student.id_student
                    INNER JOIN subject ON exam.id_subject==subject.id_subject
                    WHERE subject.name_subject = '{{name}}'
                    GROUP BY student.last_name); """)
    return result.render(name=name)

def query_find_3(name):
    result = jinja2.Template("""SELECT AVG(punkts_by_subject),name_group,subject.name_subject
            FROM exam
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            WHERE name_group = '{{name}}'
            GROUP BY subject.name_subject; """)
    return result.render(name=name)

def query_find_4():
    result = jinja2.Template("""SELECT AVG(punkts_by_subject)
            FROM exam; """)
    return result.render()

def query_find_5():
    result = jinja2.Template("""SELECT teacher.last_name,teacher.first_name,teacher.second_name,subject.name_subject
            FROM exam
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            ORDER BY teacher.last_name; """)
    return result.render()

def query_find_6(name):
    result = jinja2.Template("""SELECT student.last_name,student.first_name,student.second_name,name_group
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            WHERE name_group = '{{name}}'
            ORDER BY student.last_name; """)
    return result.render(name=name)

def query_find_7(name, subject):
    result = jinja2.Template("""SELECT student.last_name,student.first_name,student.second_name,name_group,subject.name_subject,punkts_by_subject
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            WHERE name_group = '{{name}}' AND subject.name_subject = '{{subject}}'
            ORDER BY student.last_name; """)
    return result.render(name=name, subject=subject)

def query_find_8(name, subject):
    result = jinja2.Template("""SELECT MAX(timepunkts_by_subject),student.last_name,student.first_name,student.second_name,name_group,subject.name_subject,punkts_by_subject
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            WHERE name_group = '{{name}}' AND subject.name_subject = '{{subject}}'
            GROUP BY student.last_name; """)
    return result.render(name=name, subject=subject)

def query_find_9():
    result = jinja2.Template("""SELECT subject.name_subject,student.last_name,student.first_name,student.second_name
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            ORDER BY student.last_name; """)
    return result.render()

def query_find_10():
    result = jinja2.Template("""SELECT subject.name_subject,student.last_name,teacher.last_name
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            ORDER BY student.last_name; """)
    return result.render()

def query_find_11(id):
    result = jinja2.Template("""SELECT AVG(punkts_by_subject),student.last_name,teacher.last_name
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            WHERE teacher.id_teacher = {{id}}
            GROUP BY student.last_name; """)
    return result.render(id=id)

def query_find_12():
    result = jinja2.Template("""SELECT AVG(punkts_by_subject),teacher.last_name
            FROM exam
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            GROUP BY teacher.last_name; """)
    return result.render()
