import jinja2
import random

def fill_table_student():
    temp_phone_1 = dict()
    temp_phone_2 = random.randint(1000000,9999999)
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
    result = jinja2.Template("""INSERT INTO student(id_student, first_name,second_name,last_name,phone,email,address) VALUES
            (1, 'Roman', 'Oleksandrovich', 'Astafjev', '({{temp_phone_1[0][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[0][0]}}', '{{temp_address[0][0]}}'),
            (2, 'Alina', 'Evgeniivna', 'Bezzub', '{{temp_phone_1[1][0]}}-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[1][0]}}', '{{temp_address[1][0]}}'),
            (3, 'Maria', 'Mykolaiivna', 'Bilajeva', '({{temp_phone_1[2][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[2][0]}}', '{{temp_address[2][0]}}'),
            (4, 'Valentyn', 'Oleksandrovich', 'Vlasenko', '({{temp_phone_1[3][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[3][0]}}', '{{temp_address[3][0]}}'),
            (5, 'Yulia', 'Viktorivna', 'Zolotoruchko', '({{temp_phone_1[4][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[4][0]}}', '{{temp_address[4][0]}}'),
            (6, 'Vita', 'Romazanivna', 'Ibrahimova', '({{temp_phone_1[5][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[5][0]}}', '{{temp_address[5][0]}}'),
            (7, 'Vladyslava', 'Sergiivna', 'Kysil', '({{temp_phone_1[6][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[6][0]}}', '{{temp_address[6][0]}}'),
            (8, 'Yurij', 'Volodymyrovich', 'Koval', '({{temp_phone_1[7][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[7][0]}}', '{{temp_address[7][0]}}'),
            (9, 'Viktoria', 'Volodymyrivna', 'Kornijenko', '({{temp_phone_1[8][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[8][0]}}', '{{temp_address[8][0]}}'),
            (10, 'Maria', 'Mykolaiivna', 'Kosjakova', '({{temp_phone_1[9][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[9][0]}}', '{{temp_address[9][0]}}'),
            (11, 'Oleksandr', 'Mykolayovich', 'Lytvynenko', '({{temp_phone_1[10][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[10][0]}}', '{{temp_address[10][0]}}'),
            (12, 'Anastasia', 'Viktorivna', 'Majilo', '({{temp_phone_1[11][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[11][0]}}', '{{temp_address[11][0]}}'),
            (13, 'Taras', 'Oleksandrovich', 'Myhalevich', '({{temp_phone_1[12][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[12][0]}}', '{{temp_address[12][0]}}'),
            (14, 'Anastasia', 'Vasyliivna', 'Pylypenko', '({{temp_phone_1[13][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[13][0]}}', '{{temp_address[13][0]}}'),
            (15, 'Denys', 'Igorovich', 'Popovich', '({{temp_phone_1[14][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[14][0]}}', '{{temp_address[14][0]}}'),
            (16, 'Margaryta', 'Oleksandrivna', 'Prajs', '({{temp_phone_1[15][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[15][0]}}', '{{temp_address[15][0]}}'),
            (17, 'Olga', 'Ivanivna', 'Romanchenko', '({{temp_phone_1[16][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[16][0]}}', '{{temp_address[16][0]}}'),
            (18, 'Ludmyla', 'Petrivna', 'Samusenko', '({{temp_phone_1[17][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[17][0]}}', '{{temp_address[17][0]}}'),
            (19, 'Maria', 'Valeriivna', 'Uspenska', '({{temp_phone_1[18][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[18][0]}}', '{{temp_address[18][0]}}'),
            (20, 'Yana', 'Leonidivna', 'Shevchenko', '({{temp_phone_1[19][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[19][0]}}', '{{temp_address[19][0]}}'),
            (21, 'Mykola', 'Mykolayovich', 'Bobersky', '({{temp_phone_1[20][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[20][0]}}', '{{temp_address[20][0]}}'),
            (22, 'Viktoria', 'Yuriivna', 'Druchenko', '({{temp_phone_1[21][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[21][0]}}', '{{temp_address[21][0]}}'),
            (23, 'Darina', 'Yuriivna', 'Krasnopivceva', '({{temp_phone_1[22][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[22][0]}}', '{{temp_address[22][0]}}'),
            (24, 'Valeriy', 'Valeriyovich', 'Lenko', '({{temp_phone_1[23][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[23][0]}}', '{{temp_address[23][0]}}'),
            (25, 'Yevgeniy', 'Andriyovich', 'Lytvynjuk', '({{temp_phone_1[24][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[24][0]}}', '{{temp_address[24][0]}}'),
            (26, 'Roman', 'Vasylovich', 'Makushko', '({{temp_phone_1[25][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[25][0]}}', '{{temp_address[25][0]}}'),
            (27, 'Vasyl', 'Oleksandrovich', 'Malarchuk', '({{temp_phone_1[26][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[26][0]}}', '{{temp_address[26][0]}}'),
            (28, 'Olena', 'Igorivna', 'Romanjuk', '({{temp_phone_1[27][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[27][0]}}', '{{temp_address[27][0]}}'),
            (29, 'Sergiy', 'Oleksandrovich', 'Terentjev', '({{temp_phone_1[28][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[28][0]}}', '{{temp_address[28][0]}}'),
            (30, 'Anton', 'Viktorovich', 'Yarosh', '({{temp_phone_1[29][0]}})-{{temp_phone_2}}', '{{temp_email_1}}@{{temp_email_2}}.{{temp_email_3[29][0]}}', '{{temp_address[29][0]}}'); """)
    return result.render(temp_phone_1=temp_phone_1,temp_phone_2=temp_phone_2,temp_email_1=temp_email_1,temp_email_2=temp_email_2,temp_email_3=temp_email_3, temp_address=temp_address)

def fill_table_teacher():
    result = jinja2.Template("""INSERT INTO teacher(id_teacher, first_name,second_name,last_name,phone,email,address,grade) VALUES
            (1, 'Ivan', 'Ivanovich', 'Ivanenko', '(096)-2179990', 'Ivanenko@yahoo.com', 'Kijow, ul. Chreszczatik, 7', 'Assistent'),
            (2, 'Petro', 'Petrovich', 'Petrenko', '(073)-5160913', 'Petrenko@yahoo.com', 'Kijow, ul. Wolodymyrska, 13', 'Doctor of philosophy'),
            (3, 'Sydor', 'Sydorovich', 'Sydorenko', '(050)-2203484', 'Sydorenko@yahoo.com', 'Kijow, ul.Industrialna, 23', 'Doctor of sciences'); """)
    return result.render()

def fill_table_subject():
    result = jinja2.Template("""INSERT INTO subject(id_subject, name_subject,decription_subject) VALUES
            (1, 'Mathematic', 'It is the science about the operation with numbers'),
            (2, 'Physic', 'It is the science about the learning laws of the nature'),
            (3, 'Informatic', 'It is the science about the computer technology'),
            (4, 'Chemy', 'It is the science about the building of all objects'),
            (5, 'Biology', 'It is the science about the anathomy of livingsforms'); """)
    return result.render()

def fill_table_exam():
    temp_name = ""
    result = "INSERT INTO exam(name_group,id_teacher,id_subject,id_student,punkts_by_subject,timepunkts_by_subject) VALUES"
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
                temp_data_day = random.randint(1,30)
                temp_data_month = random.randint(1,12)
                temp_data_year = random.randint(2020, 2021)
                current = jinja2.Template("('{{temp_name}}', {{k}}, {{j}}, {{i}}, {{temp_punkt}}, '{{temp_data_year}}.{{temp_data_month}}.{{temp_data_day}}')")
                result += current.render(temp_name=temp_name, temp_punkt=temp_punkt, temp_data_day=temp_data_day, temp_data_month=temp_data_month, temp_data_year=temp_data_year, i=i, j=j, k=k)
                result += ","
    result = result[:-1] + ";"
    return result
