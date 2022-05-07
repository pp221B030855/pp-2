import psycopg2

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='12345678',
    host="localhost",
    port="5432"
)

cur = con.cursor()

def pattern(pt, method):
    if method == 1:
        cur.execute(f'''SELECT "LAST NAME", "FIRST NAME", "NUMBER" FROM phonebook WHERE "LAST NAME" LIKE '{pt}%' ''')
    if method == 2:
        cur.execute(f'''SELECT "LAST NAME", "FIRST NAME", "NUMBER" FROM phonebook WHERE "FIRST NAME" LIKE '{pt}%' ''')
    if method == 3:
        cur.execute(f'''SELECT "LAST NAME", "FIRST NAME", "NUMBER" FROM phonebook WHERE "NUMBER" LIKE '{pt}%' ''')                
    rows = cur.fetchall()
    for i in rows:
        print(i) 

def add(new_user):
    cur.execute('''SELECT id, "LAST NAME", "FIRST NAME", "NUMBER" from PHONEBOOK''')
    data = cur.fetchall()
    for d in data:
        if int(d[0]) == int(new_user[0]):
            cur.execute(f"DELETE from PHONEBOOK where id={new_user[0]}")                                
            cur.execute(f'''INSERT INTO PHONEBOOK (ID, "LAST NAME", "FIRST NAME", "NUMBER") VALUES({new_user[0]}, '{new_user[1]}', '{new_user[2]}', '{new_user[3]}')''')
            con.commit()    

def querying():
        cur.execute('''SELECT id, "LAST NAME", "FIRST NAME", "NUMBER" from PHONEBOOK''')
        rows = cur.fetchall()
        id = int(input('Insert id: '))
        for row in rows:
            if row[0] == id:
                print("ID =", row[0], end = ', ')
                print("Last name =", row[1], end = ', ')
                print("First name =", row[2], end = ', ')
                print("Number =", row[3])

def delete(goal, method):
    cur.execute('''SELECT id, "LAST NAME", "FIRST NAME", "NUMBER" from PHONEBOOK''')
    rows = cur.fetchall()     
    for row in rows:
        if row[2] == goal and method == 1:
            cur.execute(f"DELETE from PHONEBOOK where id={row[0]}")
            print("Data successfully deleted")
        if row[3] == goal and method == 2:
            cur.execute(f"DELETE from PHONEBOOK where id={row[0]}")
            print("Data successfully deleted")            
    con.commit()

dic = {1 : 'name', 2 : 'phone'}

insert = int(input("1 - Seacrh by pattern (part of name)\n2 - add new user\n3 - add many users\n4 - querying data from the table\n5 - delete data from tables by username or phone\n"))
if insert == 1: 
    method = int(input('Choose one option: 1 - surname, 2 - name, 3 - number: '))
    pt = input('Input your pattern: ')
    pattern(pt, method)   
elif insert == 2: 
    new_user = list(map(str, input('Input your data (ID, Last Name, First Name, Number)\n').split()))
    add(new_user)
    print("New user successfully added")
elif insert == 3:
    number = int(input("Now many users do you want to add?\n"))
    for i in range(1,number+1):
        user = list(map(str, input(f'Input your data for user {i} (ID, Last Name, First Name, Number)\n').split()))
        add(user)
    print(f'Added {number} new users')    
elif insert == 4:
    querying()
elif insert == 5: 
    method = int(input("Delete by 1 - name, 2 - phone: "))
    goal = input(f'{dic[method]}: ')
    delete(goal, int(method))