from alembic import migration
from alembic.operations import ops
from alembic import op
from alembic import context, config
from sqlalchemy.orm import sessionmaker
from hw9_2 import *                 # creating tables
from hw9_3 import *                 # filling tables
from hw9_4 import *                 # searching in tables

def create_connection():
    engine = create_engine("sqlite:///studentdb.db", echo=True)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    return session

def main():
    while True:
        answer = input("What're You doing with database: ")
        if answer == "create db" or answer == "fill db":
            session = create_connection()
            with session.begin() as session:
                fill_table_student(session)
                fill_table_subject(session)
                fill_table_teacher(session)
                fill_table_exam(session)
                session.commit()
        elif answer == "list marks all":
            session = create_connection()
            with session.begin() as session:
                print(query_list_marks_all(session))
        elif answer == "list students":
            session = create_connection()
            with session.begin() as session:
                #q = session.query(Student).all()
                print(query_list_students(session))
        elif answer == "list teachers":
            session = create_connection()
            with session.begin() as session:
                print(query_list_teachers(session))
        elif answer == "list subjects":
            session = create_connection()
            with session.begin() as session:
                print(query_list_subjects(session))
        elif answer == "query 1":
            for id in range(1, 6):
                query_find_1(id)           # 5 студентов с наибольшим средним баллом по всем предметам
        elif answer == "query 2":
            answer1 = input("which is subject? ")
            query_find_2(answer1)          # 1 студент с наивысшим средним баллом по одному предмету.
        elif answer == "query 3":
            answer1 = input("which is group? ")
            query_find_3(answer1)          # средний балл в группе по одному предмету
        elif answer == "query 4":
            query_find_4()                 # Средний балл в потоке
        elif answer == "query 5":
            query_find_5()                 # Какие курсы читает преподаватель
        elif answer == "query 6":
            answer1 = input("which is group? ")
            query_find_6(answer1)          # Список студентов в группе
        elif answer == "query 7":
            answer1 = input("which is group? ")
            answer2 = input("which is subject? ")
            query_find_7(answer1, answer2) # Оценки студентов в группе по предмету
        elif answer == "query 8":
            answer1 = input("which is group? ")
            answer2 = input("which is subject? ")
            query_find_8(answer1, answer2) # Оценки студентов в группе по предмету на последнем занятии
        elif answer == "query 9":
            query_find_9()                 # Список курсов, которые посещает студент
        elif answer == "query 10":
            query_find_10()                # Список курсов, которые студенту читает преподаватель
        elif answer == "query 11":
            for id in range(1, 4):
                query_find_11(id)          # Средний балл, который преподаватель ставит студенту
        elif answer == "query 12":
            query_find_12()                # Средний балл, который ставит преподаватель
        elif answer == "exit":
            break

if __name__ == "__main__":
    main()
