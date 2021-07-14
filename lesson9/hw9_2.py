import alembic
from sqlalchemy import *

def create_table_student(metadata):
    students = Table("student", metadata,
                    Column("id_student", INTEGER, primary_key=True, nullable=False),
                    Column("first_name", VARCHAR(50), nullable=False),
                    Column("second_name", VARCHAR(50), nullable=False),
                    Column("last_name", VARCHAR(50), nullable=False),
                    Column("phone", VARCHAR(50), nullable=True),
                    Column("email", VARCHAR(50), nullable=True),
                    Column("address", VARCHAR(50), nullable=True))
    return students

def create_table_teacher(metadata):
    teachers = Table("teacher", metadata,
                    Column("id_teacher", INTEGER, primary_key=True, nullable=False),
                    Column("first_name", VARCHAR(50), nullable=False),
                    Column("second_name", VARCHAR(50), nullable=False),
                    Column("last_name", VARCHAR(50), nullable=False),
                    Column("phone", VARCHAR(50), nullable=True),
                    Column("email", VARCHAR(50), nullable=True),
                    Column("address", VARCHAR(50), nullable=True),
                    Column("grade", VARCHAR(30), nullable=True))
    return teachers

def create_table_subject(metadata):
    subjects = Table("subject", metadata,
                    Column("id_subject", INTEGER, primary_key=True, nullable=False),
                    Column("name_subject", VARCHAR(50), nullable=False),
                    Column("decription_subject", VARCHAR(500), nullable=True))
    return subjects

def create_table_exam(metadata):
    exams = Table("exam", metadata,
                    Column("id_exam", INTEGER, primary_key=True, nullable=False),
                    Column("name_group", VARCHAR(10), nullable=False),
                    Column("id_student", None, ForeignKey("student.id_student"), nullable=False),
                    Column("id_teacher", None, ForeignKey("teacher.id_teacher"), nullable=False),
                    Column("id_subject", None, ForeignKey("subject.id_subject"), nullable=False),
                    Column("punkts_by_subject", INTEGER, nullable=True),
                    Column("timepunkts_by_subject", DATE, nullable=True))
    return exams
