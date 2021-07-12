def create_table_student():
    return """CREATE TABLE IF NOT EXISTS student(
        id_student INTEGER PRIMARY KEY NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        second_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        phone VARCHAR(50),
        email VARCHAR(50),
        address VARCHAR(50));"""

def create_table_teacher():
    return """CREATE TABLE IF NOT EXISTS teacher(
        id_teacher INTEGER PRIMARY KEY NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        second_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        phone VARCHAR(50),
        email VARCHAR(50),
        address VARCHAR(50),
        grade VARCHAR(30));"""

def create_table_subject():
    return """CREATE TABLE IF NOT EXISTS subject(
        id_subject INTEGER PRIMARY KEY NOT NULL,
        name_subject VARCHAR(50) NOT NULL,
        decription_subject VARCHAR(500));"""

def create_table_exam():
    return """CREATE TABLE IF NOT EXISTS exam(
        id_exam INTEGER PRIMARY KEY NOT NULL,
        name_group VARCHAR(10) NOT NULL,
        id_student INTEGER,
        id_teacher INTEGER,
        id_subject INTEGER,
        punkts_by_subject INTEGER,
        timepunkts_by_subject DATE,
        FOREIGN KEY (id_student) REFERENCES student (id_student) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (id_teacher) REFERENCES teacher (id_teacher) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (id_subject) REFERENCES subject (id_subject) ON DELETE SET NULL ON UPDATE CASCADE);"""
