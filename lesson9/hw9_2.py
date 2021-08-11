from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id_student = Column("id_student", INTEGER, primary_key=True, nullable=False)
    first_name = Column("first_name", VARCHAR(50), nullable=False)
    second_name = Column("second_name", VARCHAR(50), nullable=False)
    last_name = Column("last_name", VARCHAR(50), nullable=False)
    phone = Column("phone", VARCHAR(50), nullable=True)
    email = Column("email", VARCHAR(50), nullable=True)
    address = Column("address", VARCHAR(50), nullable=True)
    def __repr__(self):
        return "Student(id_student='{}', first_name='{}', second_name='{}', last_name='{}', phone='{}', email='{}', address='{}')\n".format(self.id_student,self.first_name,self.second_name,self.last_name,self.phone,self.email,self.address)

class Teacher(Base):
    __tablename__ = "teachers"
    id_teacher = Column("id_teacher", INTEGER, primary_key=True, nullable=False)
    first_name = Column("first_name", VARCHAR(50), nullable=False)
    second_name = Column("second_name", VARCHAR(50), nullable=False)
    last_name = Column("last_name", VARCHAR(50), nullable=False)
    phone = Column("phone", VARCHAR(50), nullable=True)
    email = Column("email", VARCHAR(50), nullable=True)
    address = Column("address", VARCHAR(50), nullable=True)
    grade = Column("grade", VARCHAR(30), nullable=True)
    def __repr__(self):
        return "Teacher(id_teacher='{}', first_name='{}', second_name='{}', last_name='{}', phone='{}', email='{}', address='{}',grade='{}')\n".format(self.id_teacher,self.first_name,self.second_name,self.last_name,self.phone,self.email,self.address,self.grade)

class Subject(Base):
    __tablename__ = "subjects"
    id_subject = Column("id_subject", INTEGER, primary_key=True, nullable=False)
    name_subject = Column("name_subject", VARCHAR(50), nullable=False)
    decription_subject = Column("decription_subject", VARCHAR(500), nullable=True)
    def __repr__(self):
        return "Subject(id_subject='{}', name_subject='{}', decription_subject='{}')\n".format(self.id_subject,self.name_subject,self.decription_subject)

class Exam(Base):
    __tablename__ = "exams"
    id_exam = Column("id_exam", INTEGER, primary_key=True, nullable=False)
    name_group = Column("name_group", VARCHAR(10), nullable=False)
    id_student = Column("id_student", None, ForeignKey("students.id_student"), nullable=False)
    id_teacher = Column("id_teacher", None, ForeignKey("teachers.id_teacher"), nullable=False)
    id_subject = Column("id_subject", None, ForeignKey("subjects.id_subject"), nullable=False)
    punkts_by_subject = Column("punkts_by_subject", INTEGER, nullable=True)
    timepunkts_by_subject = Column("timepunkts_by_subject", DATE, nullable=True)
    def __repr__(self):
        return "Exam(id_exam='{}', name_group='{}', id_student='{}', id_teacher='{}', id_subject='{}', punkts_by_subject='{}', timepunkts_by_subject='{}')\n".format(self.id_exam,self.name_group,self.id_student,self.id_teacher,self.id_subject,self.punkts_by_subject,self.timepunkts_by_subject)
