import sqlite3
from contextlib import contextmanager
from hw8_2 import *                 # creating tables
from hw8_3 import *                 # filling tables
from hw8_4 import *                 # searching in tables
from sqlite3 import Error

def sqlquery(conn, sqlquery):
    try:
        c = conn.cursor()
        c.execute(sqlquery)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

@contextmanager
def create_connection(student_db):
    try:
        my_connection = sqlite3.connect(student_db)
        print(sqlite3.version)
        yield my_connection
        my_connection.commit()
    except Error as e:
        my_connection.rollback()
        print(e)
    finally:
        my_connection.close()

def main():
    database = "./studentdb.db"
    with create_connection(database) as my_connection:
        if my_connection is not None:
            while True:
                answer = input("What're You doing with database: ")
                if answer == "create db":
                    sqlquery(my_connection, create_table_student())
                    sqlquery(my_connection, create_table_subject())
                    sqlquery(my_connection, create_table_teacher())
                    sqlquery(my_connection, create_table_exam())
                elif answer == "fill db":
                    sqlquery(my_connection, fill_table_student())
                    sqlquery(my_connection, fill_table_subject())
                    sqlquery(my_connection, fill_table_teacher())
                    sqlquery(my_connection, fill_table_exam())
                elif answer == "list marks all":
                    sqlquery(my_connection, query_list_marks_all())
                elif answer == "list students":
                    sqlquery(my_connection, query_list_students())
                elif answer == "list teachers":
                    sqlquery(my_connection, query_list_teachers())
                elif answer == "list subjects":
                    sqlquery(my_connection, query_list_subjects())
                elif answer == "query 1":
                    for id in range(1, 6):
                        sqlquery(my_connection, query_find_1(id))           # 5 студентов с наибольшим средним баллом по всем предметам
                elif answer == "query 2":
                    answer1 = input("which is subject? ")
                    sqlquery(my_connection, query_find_2(answer1))          # 1 студент с наивысшим средним баллом по одному предмету.
                elif answer == "query 3":
                    answer1 = input("which is group? ")
                    sqlquery(my_connection, query_find_3(answer1))          # средний балл в группе по одному предмету
                elif answer == "query 4":
                    sqlquery(my_connection, query_find_4())                 # Средний балл в потоке
                elif answer == "query 5":
                    sqlquery(my_connection, query_find_5())                 # Какие курсы читает преподаватель
                elif answer == "query 6":
                    answer1 = input("which is group? ")
                    sqlquery(my_connection, query_find_6(answer1))          # Список студентов в группе
                elif answer == "query 7":
                    answer1 = input("which is group? ")
                    answer2 = input("which is subject? ")
                    sqlquery(my_connection, query_find_7(answer1, answer2)) # Оценки студентов в группе по предмету
                elif answer == "query 8":
                    answer1 = input("which is group? ")
                    answer2 = input("which is subject? ")
                    sqlquery(my_connection, query_find_8(answer1, answer2)) # Оценки студентов в группе по предмету на последнем занятии
                elif answer == "query 9":
                    sqlquery(my_connection, query_find_9())                 # Список курсов, которые посещает студент
                elif answer == "query 10":
                    sqlquery(my_connection, query_find_10())                # Список курсов, которые студенту читает преподаватель
                elif answer == "query 11":
                    for id in range(1, 4):
                        sqlquery(my_connection, query_find_11(id))          # Средний балл, который преподаватель ставит студенту
                elif answer == "query 12":
                    sqlquery(my_connection, query_find_12())                # Средний балл, который ставит преподаватель
                elif answer == "exit":
                    break
                else:
                    print("Error! You're maked the misstake by inputing")
        else:
            print(f"Error! The connection with database {database} are not created!")

if __name__ == "__main__":
    main()
