from tabnanny import check
import psycopg2 
import csv

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='12345678',
    host="localhost",
    port="5432"
)

cur = con.cursor()
print('You have successfully connected to the databases')
# CREATE TABLE 
# cur.execute("DROP TABLE PHONEBOOK")
# cur.execute('''CREATE TABLE PHONEBOOK
#     (ID INT PRIMARY KEY NOT NULL,
#     "LAST NAME" TEXT NOT NULL,
#     "FIRST NAME" TEXT NOT NULL,
#     "NUMBER" TEXT NOT NULL);'''
# )

dic = {1 : "LAST NAME", 2 : "FIRST NAME", 3 : "NUMBER"}

while True:
    v = int(input('1 - Enter data\n2 - Change data\n3 - Querying data\n4 - Delete data\n5 - Exit\n'))
    if v == 1:
        method = int(input("Which method: 1 - console, 2 - csv file: "))
        if method == 1: 
            ls = list(map(str, input('Input your data (ID, Last Name, First Name, Number)\n').split()))
            try:
                cur.execute(f'''INSERT INTO PHONEBOOK (ID, "LAST NAME", "FIRST NAME", "NUMBER") VALUES({ls[0]}, '{ls[1]}', '{ls[2]}', '{ls[3]}')''')
                print('Data successfully inserted\n')
            except:
                print('Ops, this id already exist\n')
            con.commit()

        if method == 2:
            results = []
            file = open('data.csv')
            csvreader = csv.reader(file)
            rows = []
            for row in csvreader:
                rows.append(row)
            for row in rows[1:]:
                    cur.execute('''SELECT id, "LAST NAME", "FIRST NAME", "NUMBER" from PHONEBOOK''')
                    data = cur.fetchall()
                    check = True
                    for d in data:
                        if int(d[0]) == int(row[0]):
                            cur.execute(f"DELETE from PHONEBOOK where id={row[0]}")                                
                            cur.execute(f'''INSERT INTO PHONEBOOK (ID, "LAST NAME", "FIRST NAME", "NUMBER") VALUES({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}')''')
                            con.commit()
                            check = False
                    if check: 
                        cur.execute(f'''INSERT INTO PHONEBOOK (ID, "LAST NAME", "FIRST NAME", "NUMBER") VALUES({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}')''') 
                    con.commit() 
            print('Data successfully inserted\n')              
        
    if v == 2:
        id = input('Insert id: ')
        x = int(input('1 - Last name\n2 - First name\n3 - number\n'))
        new = input("Input new data: ")
        cur.execute(f'''Update PHONEBOOK set "{dic[x]}" = '{new}' where ID = {id}''')
        con.commit()
        print('Data successfully changed\n')            


    if v == 3:
        cur.execute('''SELECT id, "LAST NAME", "FIRST NAME", "NUMBER" from PHONEBOOK''')
        rows = cur.fetchall()
        id = int(input('Insert id: '))
        for row in rows:
            if row[0] == id:
                print("ID =", row[0], end = ', ')
                print("Last name =", row[1], end = ', ')
                print("First name =", row[2], end = ', ')
                print("Number =", row[3], '\n')
        con.commit()        
    if v == 4:
        cur.execute('''SELECT id, "LAST NAME", "FIRST NAME", "NUMBER" from PHONEBOOK''')
        rows = cur.fetchall()     
        name = input('username of phone: ')
        for row in rows:
            if row[2] == name:
                cur.execute(f"DELETE from PHONEBOOK where id={row[0]}")
                print("Data successfully deleted\n")
        con.commit()        
    if v == 5:
        exit()    