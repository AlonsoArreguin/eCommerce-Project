from InventoryClass import Inventory, connection, cursor
from UserClass import User
from CartClass import Cart

#create database tables if they don't exist here
connection.execute('''
    CREATE TABLE IF NOT EXISTS inventory(
        isbn integer PRIMARY KEY,
        title text NOT NULL, 
        author text NOT NULL,
        genre text NOT NULL,
        pages integer NOT NULL,
        releasedate date NOT NULL,
        stock integer NOT NULL)
        ''')
connection.execute('''
    CREATE TABLE IF NOT EXISTS user(
        userid text PRIMARY KEY,
        email text NOT NULL,
        password text NOT NULL,
        firstname text NOT NULL,
        lastname text NOT NULL,
        address text NOT NULL,
        city text NOT NULL,
        state text NOT NULL,
        zip integer NOT NULL,
        payment text NOT NULL)
        ''')
connection.execute('''
    CREATE TABLE IF NOT EXISTS cart(
        userid integer,
        isbn integer,
        quantity integer NOT NULL,
        FOREIGN KEY(userid) REFERENCES user(userid)
        FOREIGN KEY(isbn) REFERENCES inventory(isbn))
        ''')
#create sample datasets here if they do not exist
exiting = False
user = User()
def startMenu():
    while not user.loggedIn:
        print("\nStart Menu: ")
        print("1. Login")
        print("2. Create Account")
        print("3. Logout")
        #User inputs answer
        try:
            sel = int(input("Please select an option: "))
        except ValueError:
            sel = 0
        #Options
        if sel == 1:
            user.login()
        elif sel == 2:
            user.createAccount()
        elif sel == 3:
            global exiting
            exiting = True
            break
        else:
            print("Error. Invalid option.")
while not exiting:
    startMenu()

cursor.close()
connection.close()
    
