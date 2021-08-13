from sqlalchemy.orm import query
from sqlalchemy.sql import func
from hw9_2 import *                 # creating tables

def query_list_marks_all(session):
    return query.Query([Student, Teacher, Subject, Exam,], session).all()

def query_list_students(session):
    return query.Query([Student,], session).all()

def query_list_teachers(session):
    return query.Query([Teacher,], session).all()

def query_list_subjects(session):
    return query.Query([Subject,], session).all()

def query_find_1(session, id):
    '''result = jinja2.Template("""SELECT student,MAX(avg_mark),subject
            FROM (SELECT AVG(punkts_by_subject) as avg_mark,student.last_name as student,subject.name_subject as subject
                    FROM exam
                    INNER JOIN student ON exam.id_student==student.id_student
                    INNER JOIN subject ON exam.id_subject==subject.id_subject
                    WHERE subject.id_subject = {{id}}
                    GROUP BY student.last_name); """)
    return result.render(id=id)
    '''
    sub_query = query.Query([func.avg(Exam.punkts_by_subject).label("avg_mark"), Student.last_name.label("student"), Subject.name_subject.label("subject")], session).select_from(Exam).join(Student).join(Subject).filter(Subject.id_subject == id).group_by(Student.last_name)
    return query.Query([column("student"), func.max(column("avg_mark")),column("subject")], session).select_from(sub_query).all()

def query_find_2(session, name):
    '''result = jinja2.Template("""SELECT student,MAX(avg_mark),subject
            FROM (SELECT AVG(punkts_by_subject) as avg_mark,student.last_name as student,subject.name_subject as subject
                    FROM exam
                    INNER JOIN student ON exam.id_student==student.id_student
                    INNER JOIN subject ON exam.id_subject==subject.id_subject
                    WHERE subject.name_subject = '{{name}}'
                    GROUP BY student.last_name); """)
    return result.render(name=name)
    '''
    sub_query = query.Query([func.avg(Exam.punkts_by_subject).label("avg_mark"), Student.last_name.label("student"), Subject.name_subject.label("subject")], session).select_from(Exam).join(Student).join(Subject).filter(Subject.name_subject == name).group_by(Student.last_name)
    return query.Query([column("student"), func.max(column("avg_mark")),column("subject")], session).select_from(sub_query).all()

def query_find_3(session, name):
    '''result = jinja2.Template("""SELECT AVG(punkts_by_subject),name_group,subject.name_subject
            FROM exam
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            WHERE name_group = '{{name}}'
            GROUP BY subject.name_subject; """)
    return result.render(name=name)
    '''
    return query.Query([func.avg(Exam.punkts_by_subject),Exam.name_group,Subject.name_subject], session).select_from(Exam).join(Subject).filter(Exam.name_group == name).group_by(Subject.name_subject).all()

def query_find_4(session):
    '''result = jinja2.Template("""SELECT AVG(punkts_by_subject)
            FROM exam; """)
    return result.render()
    '''
    return query.Query([func.avg(Exam.punkts_by_subject)], session).select_from(Exam).all()

def query_find_5(session):
    '''result = jinja2.Template("""SELECT teacher.last_name,teacher.first_name,teacher.second_name,subject.name_subject
            FROM exam
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            ORDER BY teacher.last_name; """)
    return result.render()
    '''
    return query.Query([Teacher.last_name,Teacher.first_name,Teacher.second_name,Subject.name_subject], session).select_from(Exam).join(Subject).join(Teacher).order_by(Teacher.last_name).all()

def query_find_6(session, name):
    '''result = jinja2.Template("""SELECT student.last_name,student.first_name,student.second_name,name_group
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            WHERE name_group = '{{name}}'
            ORDER BY student.last_name; """)
    return result.render(name=name)
    '''
    return query.Query([Student.last_name,Student.first_name,Student.second_name,Exam.name_group], session).select_from(Exam).join(Student).filter(Exam.name_group == name).order_by(Student.last_name).all()

def query_find_7(session, name, subject):
    '''result = jinja2.Template("""SELECT student.last_name,student.first_name,student.second_name,name_group,subject.name_subject,punkts_by_subject
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            WHERE name_group = '{{name}}' AND subject.name_subject = '{{subject}}'
            ORDER BY student.last_name; """)
    return result.render(name=name, subject=subject)
    '''
    return query.Query([Student.last_name,Student.first_name,Student.second_name,Exam.name_group,Subject.name_subject,Exam.punkts_by_subject], session).select_from(Exam).join(Student).join(Subject).filter(Exam.name_group==name, Subject.name_subject == subject).order_by(Student.last_name).all()

def query_find_8(session, name, subject):
    '''result = jinja2.Template("""SELECT MAX(timepunkts_by_subject),student.last_name,student.first_name,student.second_name,name_group,subject.name_subject,punkts_by_subject
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            WHERE name_group = '{{name}}' AND subject.name_subject = '{{subject}}'
            GROUP BY student.last_name; """)
    return result.render(name=name, subject=subject)
    '''
    return query.Query([func.max(Exam.timepunkts_by_subject),Student.last_name,Student.first_name,Student.second_name,Exam.name_group,Subject.name_subject,Exam.punkts_by_subject], session).select_from(Exam).join(Student).join(Subject).filter(Exam.name_group == name, Subject.name_subject == subject).group_by(Student.last_name).all()

def query_find_9(session):
    '''result = jinja2.Template("""SELECT subject.name_subject,student.last_name,student.first_name,student.second_name
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            ORDER BY student.last_name; """)
    return result.render()
    '''
    return query.Query([Subject.name_subject,Student.last_name,Student.first_name,Student.second_name], session).select_from(Exam).join(Student).join(Subject).order_by(Student.last_name).all()

def query_find_10(session):
    '''result = jinja2.Template("""SELECT subject.name_subject,student.last_name,teacher.last_name
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN subject ON exam.id_subject==subject.id_subject
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            ORDER BY student.last_name; """)
    return result.render()
    '''
    return query.Query([Subject.name_subject,Student.last_name,Teacher.last_name], session).select_from(Exam).join(Student).join(Subject).join(Teacher).order_by(Student.last_name).all()

def query_find_11(session, id):
    '''result = jinja2.Template("""SELECT AVG(punkts_by_subject),student.last_name,teacher.last_name
            FROM exam
            INNER JOIN student ON exam.id_student==student.id_student
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            WHERE teacher.id_teacher = {{id}}
            GROUP BY student.last_name; """)
    return result.render(id=id)
    '''
    return query.Query([func.avg(Exam.punkts_by_subject),Student.last_name,Teacher.last_name], session).select_from(Exam).join(Student).join(Teacher).filter(Teacher.id_teacher == id).group_by(Student.last_name).all()

def query_find_12(session):
    '''result = jinja2.Template("""SELECT AVG(punkts_by_subject),teacher.last_name
            FROM exam
            INNER JOIN teacher ON exam.id_teacher==teacher.id_teacher
            GROUP BY teacher.last_name; """)
    return result.render()
    '''
    return query.Query([func.avg(Exam.punkts_by_subject),Teacher.last_name], session).select_from(Exam).join(Teacher).group_by(Teacher.last_name).all()
