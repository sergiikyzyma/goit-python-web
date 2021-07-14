import alembic
import jinja2
import random
import datetime
from sqlalchemy import *

def fill_table_student(engine, students):
    temp_phone_1 = dict()
    temp_phone_2 = str(random.randint(1000000,9999999))
    temp_email_k1 = random.randint(1,30)
    temp_email_k2 = random.randint(1,20)
    temp_email_x1 = random.sample('abcdefgh.ijklmnop-qrstuvwxyz_0123456789', k=temp_email_k1)
    temp_email_x2 = random.sample('abcdefghijklmnopqrstuvwxyz', k=temp_email_k2)
    temp_email_1 = ""
    for i in range(0, len(temp_email_x1)):
        temp_email_1 += temp_email_x1[i]
    temp_email_2 = ""
    for i in range(0, len(temp_email_x2)):
        temp_email_2 += temp_email_x2[i]
    temp_email_3 = dict()
    temp_address = dict()
    for j in range(0, 30):
        temp_phone_1[j] = random.sample({'053', '063', '073', '050', '067', '068', '095', '096', '097', '098'}, k=1)
        temp_email_3[j] = random.sample({'com', 'org', 'net', 'gov', 'ua', 'ru', 'pl', 'us', 'de'}, k=1)
        temp_address[j] = random.sample({'Kijow', 'Winnica', 'Charkow', 'Odessa', 'Lwow', 'Poltava', 'Dniepr', 'Stanislawow', 'Zytomierz'}, k=1)
    ins1 = students.insert().values(first_name='Roman', second_name='Oleksandrovich', last_name='Astafjev', phone='('+temp_phone_1[0][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[0][0], address=temp_address[0][0])
    ins2 = students.insert().values(first_name='Alina', second_name='Evgeniivna', last_name='Bezzub', phone='('+temp_phone_1[1][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[1][0], address=temp_address[1][0])
    ins3 = students.insert().values(first_name='Maria', second_name='Mykolaiivna', last_name='Bilajeva', phone='('+temp_phone_1[2][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[2][0], address=temp_address[2][0])
    ins4 = students.insert().values(first_name='Valentyn', second_name='Oleksandrovich', last_name='Vlasenko', phone='('+temp_phone_1[3][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[3][0], address=temp_address[3][0])
    ins5 = students.insert().values(first_name='Yulia', second_name='Viktorivna', last_name='Zolotoruchko', phone='('+temp_phone_1[4][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[4][0], address=temp_address[4][0])
    ins6 = students.insert().values(first_name='Vita', second_name='Romazanivna', last_name='Ibrahimova', phone='('+temp_phone_1[5][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[5][0], address=temp_address[5][0])
    ins7 = students.insert().values(first_name='Vladyslava', second_name='Sergiivna', last_name='Kysil', phone='('+temp_phone_1[6][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[6][0], address=temp_address[6][0])
    ins8 = students.insert().values(first_name='Yurij', second_name='Volodymyrovich', last_name='Koval', phone='('+temp_phone_1[7][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[7][0], address=temp_address[7][0])
    ins9 = students.insert().values(first_name='Viktoria', second_name='Volodymyrivna', last_name='Kornijenko', phone='('+temp_phone_1[8][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[8][0], address=temp_address[8][0])
    ins10 = students.insert().values(first_name='Maria', second_name='Mykolaiivna', last_name='Kosjakova', phone='('+temp_phone_1[9][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[9][0], address=temp_address[9][0])
    ins11 = students.insert().values(first_name='Oleksandr', second_name='Mykolayovich', last_name='Lytvynenko', phone='('+temp_phone_1[10][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[10][0], address=temp_address[10][0])
    ins12 = students.insert().values(first_name='Anastasia', second_name='Viktorivna', last_name='Majilo', phone='('+temp_phone_1[11][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[11][0], address=temp_address[11][0])
    ins13 = students.insert().values(first_name='Taras', second_name='Oleksandrovich', last_name='Myhalevich', phone='('+temp_phone_1[12][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[12][0], address=temp_address[12][0])
    ins14 = students.insert().values(first_name='Anastasia', second_name='Vasyliivna', last_name='Pylypenko', phone='('+temp_phone_1[13][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[13][0], address=temp_address[13][0])
    ins15 = students.insert().values(first_name='Denys', second_name='Igorovich', last_name='Popovich', phone='('+temp_phone_1[14][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[14][0], address=temp_address[14][0])
    ins16 = students.insert().values(first_name='Margaryta', second_name='Oleksandrivna', last_name='Prajs', phone='('+temp_phone_1[15][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[15][0], address=temp_address[15][0])
    ins17 = students.insert().values(first_name='Olga', second_name='Ivanivna', last_name='Romanchenko', phone='('+temp_phone_1[16][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[16][0], address=temp_address[16][0])
    ins18 = students.insert().values(first_name='Ludmyla', second_name='Petrivna', last_name='Samusenko', phone='('+temp_phone_1[17][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[17][0], address=temp_address[17][0])
    ins19 = students.insert().values(first_name='Maria', second_name='Valeriivna', last_name='Uspenska', phone='('+temp_phone_1[18][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[18][0], address=temp_address[18][0])
    ins20 = students.insert().values(first_name='Yana', second_name='Leonidivna', last_name='Shevchenko', phone='('+temp_phone_1[19][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[19][0], address=temp_address[19][0])
    ins21 = students.insert().values(first_name='Mykola', second_name='Mykolayovich', last_name='Bobersky', phone='('+temp_phone_1[20][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[20][0], address=temp_address[20][0])
    ins22 = students.insert().values(first_name='Viktoria', second_name='Yuriivna', last_name='Druchenko', phone='('+temp_phone_1[21][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[21][0], address=temp_address[21][0])
    ins23 = students.insert().values(first_name='Darina', second_name='Yuriivna', last_name='Krasnopivceva', phone='('+temp_phone_1[22][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[22][0], address=temp_address[22][0])
    ins24 = students.insert().values(first_name='Valeriy', second_name='Valeriyovich', last_name='Lenko', phone='('+temp_phone_1[23][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[23][0], address=temp_address[23][0])
    ins25 = students.insert().values(first_name='Yevgeniy', second_name='Andriyovich', last_name='Lytvynjuk', phone='('+temp_phone_1[24][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[24][0], address=temp_address[24][0])
    ins26 = students.insert().values(first_name='Roman', second_name='Vasylovich', last_name='Makushko', phone='('+temp_phone_1[25][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[25][0], address=temp_address[25][0])
    ins27 = students.insert().values(first_name='Vasyl', second_name='Oleksandrovich', last_name='Malarchuk', phone='('+temp_phone_1[26][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[26][0], address=temp_address[26][0])
    ins28 = students.insert().values(first_name='Olena', second_name='Igorivna', last_name='Romanjuk', phone='('+temp_phone_1[27][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[27][0], address=temp_address[27][0])
    ins29 = students.insert().values(first_name='Sergiy', second_name='Oleksandrovich', last_name='Terentjev', phone='('+temp_phone_1[28][0]+')-'+temp_phone_2, email=temp_email_1+'@'+temp_email_2+'.'+temp_email_3[28][0], address=temp_address[28][0])
    ins30 = students.insert().values(first_name='Anton', second_name='Viktorovich', last_name='Yarosh', phone='(' + temp_phone_1[29][0] + ')-' + temp_phone_2, email=temp_email_1 + '@' + temp_email_2 + '.' + temp_email_3[29][0], address=temp_address[29][0])
    conn = engine.connect()
    
def fill_table_teacher(engine, teachers):
    ins1 = teachers.insert().values(first_name='Ivan', second_name='Ivanovich', last_name='Ivanenko', phone='(096)-2179990', email='Ivanenko@yahoo.com', address='Kijow, ul. Chreszczatik, 7', grade='Assistent')
    ins2 = teachers.insert().values(first_name='Petro', second_name='Petrovich', last_name='Petrenko', phone='(073)-5160913', email='Petrenko@yahoo.com', address='Kijow, ul. Wolodymyrska, 13', grade='Doctor of philosophy')
    ins3 = teachers.insert().values(first_name='Sydor', second_name='Sydorovich', last_name='Sydorenko', phone='(050)-2203484', email='Sydorenko@yahoo.com', address='Kijow, ul.Industrialna, 23', grade='Doctor of sciences')
    conn = engine.connect()

def fill_table_subject(engine, subjects):
    ins1 = subjects.insert().values(name_subject='Mathematic',decription_subject='It is the science about the operation with numbers')
    ins2 = subjects.insert().values(name_subject='Physic',decription_subject='It is the science about the learning laws of the nature')
    ins3 = subjects.insert().values(name_subject='Informatic',decription_subject='It is the science about the computer technology')
    ins4 = subjects.insert().values(name_subject='Chemy',decription_subject='It is the science about the building of all objects')
    ins5 = subjects.insert().values(name_subject='Biology', decription_subject='It is the science about the anathomy of livingsforms')
    conn = engine.connect()

def fill_table_exam(engine, exams):
    temp_name = ""
    for i in range(1, 31):  
        for j in range(1, 6):
            for k in range(1, 4):
                if i <= 10:
                    temp_name = 'Tech101'
                elif i > 10 and i <= 20:
                    temp_name = 'Tech102'
                elif i > 20:
                    temp_name = 'Tech103'
                temp_punkt = random.randint(60, 100)
                temp_data_day = str(random.randint(1,30))
                temp_data_month = str(random.randint(1,12))
                temp_data_year = str(random.randint(2020, 2021))
                if temp_data_month == '2':
                    temp_data_day = str(random.randint(1,28))
                temp_data = datetime.datetime.strptime(temp_data_year+'.'+temp_data_month+'.'+temp_data_day, "%Y.%m.%d")
                ins = exams.insert().values(name_group=temp_name,id_teacher=k,id_subject=j,id_student=i,punkts_by_subject=temp_punkt,timepunkts_by_subject=temp_data)
    conn = engine.connect()
