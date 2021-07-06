import sqlite3
from contextlib import contextmanager
from hw8_2 import * #creating tables
from hw8_3 import * #filling tables
from hw8_4 import * #searching in tables
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
                    sqlquery(my_connection, create_table_groups())
                elif answer == "fill db":
                    sqlquery(my_connection, fill_table_student())
                    sqlquery(my_connection, fill_table_subject())
                    sqlquery(my_connection, fill_table_teacher())
                    sqlquery(my_connection, fill_table_groups())
                elif answer == "find all":
                    sqlquery(my_connection, query_find_all())
                elif answer == "find 1":
                    sqlquery(my_connection, query_find_1())
                elif answer == "find 2":
                    sqlquery(my_connection, query_find_2())
                elif answer == "find 3":
                    sqlquery(my_connection, query_find_3())
                elif answer == "exit":
                    break
                else:
                    print("Error! You're maked the misstake by inputing")
        else:
            print(f"Error! The connection with database {database} are not created!")

if __name__ == "__main__":
    main()
