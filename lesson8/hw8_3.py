def fill_table_student():
    return """INSERT INTO student(fist_name,second_name,last_name,phone,email,address) VALUES
            ('Ivan', 'Ivanovich', 'Ivanov', '4365r46', 'vgcg@bdhv.com', 'Kijow'),
            ('Petro', 'Petrovich', 'Petrov', '5364577', 'vbdh@vbfhd.cpm', 'Kharkow'),
            ('Sydor', 'Sydorovich', 'Sydorov', '4453640', 'vnj@vbfv.com', 'Odessa');"""

def fill_table_teacher():
    return """INSERT INTO teacher(fist_name,second_name,last_name,phone,email,address) VALUES
            ('Ivan', 'Ivanovich', 'Ivanenko', '0962179990', 'Ivanenko@yahoo.com', 'Kijow, ul. Chreszczatik, 7'),
            ('Petro', 'Petrovich', 'Petrenko', '0735160913', 'Petrenko@yahoo.com', 'Kijow, ul. Wolodymyrska, 13'),
            ('Sydor', 'Sydorovich', 'Sydorenko', '0502203484', 'Sydorenko@yahoo.com', 'Kijow, ul.Industrialna, 23');"""

def fill_table_subject():
    return """INSERT INTO subject(name_subject,decription_subject) VALUES
            ('Mathematic', 'It is the science about the operation with numbers'),
            ('Physic', 'It is the science about the learning laws of the nature'),
            ('Informatic', 'It is the science about the computer technology'),
            ('Chemy', 'It is the science about the building of all objects'),
            ('Biology', 'It is the science about the anathomy of livingsforms');"""

def fill_table_groups():
    return """INSERT INTO groups(name_group,id_teacher,id_subject,id_student,punkts_by_subject,timepunkts_by_subject) VALUES
            ('Tech101', 1, 3, 3, 98, '28.09.2021'),
            ('Tech103', 2, 1, 3, 90, '28.09.2021'),
            ('Tech102', 3, 3, 3, 76, '28.09.2021'),
            ('Tech103', 3, 2, 1, 67, '28.09.2021'),
            ('Tech102', 2, 3, 2, 91, '28.09.2021'),
            ('Tech101', 1, 2, 3, 100, '28.09.2021'),
            ('Tech101', 2, 2, 2, 78, '28.09.2021');"""
