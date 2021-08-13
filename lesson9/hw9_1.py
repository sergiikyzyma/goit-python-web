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
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                fill_table_student(session)
                fill_table_subject(session)
                fill_table_teacher(session)
                fill_table_exam(session)
                session.commit()
        elif answer == "list marks all":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_list_marks_all(session))
        elif answer == "list students":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_list_students(session))
        elif answer == "list teachers":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_list_teachers(session))
        elif answer == "list subjects":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_list_subjects(session))
        elif answer == "query 1":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                for id in range(1, 6):
                    print(query_find_1(session, id))           # 5 студентов с наибольшим средним баллом по всем предметам
        elif answer == "query 2":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                answer1 = input("which is subject? ")
                print(query_find_2(session, answer1))          # 1 студент с наивысшим средним баллом по одному предмету.
        elif answer == "query 3":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                answer1 = input("which is group? ")
                print(query_find_3(session, answer1))          # средний балл в группе по одному предмету
        elif answer == "query 4":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_find_4(session))                 # Средний балл в потоке
        elif answer == "query 5":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_find_5(session))                 # Какие курсы читает преподаватель
        elif answer == "query 6":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                answer1 = input("which is group? ")
                print(query_find_6(session, answer1))          # Список студентов в группе
        elif answer == "query 7":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                answer1 = input("which is group? ")
                answer2 = input("which is subject? ")
                print(query_find_7(session, answer1, answer2)) # Оценки студентов в группе по предмету
        elif answer == "query 8":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                answer1 = input("which is group? ")
                answer2 = input("which is subject? ")
                print(query_find_8(session, answer1, answer2)) # Оценки студентов в группе по предмету на последнем занятии
        elif answer == "query 9":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_find_9(session))                 # Список курсов, которые посещает студент
        elif answer == "query 10":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_find_10(session))                # Список курсов, которые студенту читает преподаватель
        elif answer == "query 11":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                for id in range(1, 4):
                    print(query_find_11(session, id))          # Средний балл, который преподаватель ставит студенту
        elif answer == "query 12":
            session = create_connection()                   #creating conection with current state DB
            with session.begin() as session:
                print(query_find_12(session))                # Средний балл, который ставит преподаватель
        elif answer == "exit":
            break

if __name__ == "__main__":
    main()
