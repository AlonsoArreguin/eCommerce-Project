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
inventory = Inventory()
cart = Cart()
def startMenu():
    while not user.loggedIn:
        print("\nStart Menu: ")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
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

def mainMenu():
    while user.loggedIn:
        #main menu
        print("\nMain Menu: ")
        print("1. View Account Information ")
        print("2. Inventory Information ")
        print("3. Cart Information ")
        print("4. Log out")
        #input
        try:
            sel = int(input("Please select an option: "))
        except ValueError:
            sel = 0
        #options
        if sel == 1:
            user.viewAccountInformation()
        elif sel == 2:
            inventoryMenu()
        elif sel == 3:
            cartMenu()
        elif sel == 4:
            user.logout()
        else:
            print("Invalid option")

def inventoryMenu():
    while user.loggedIn:
        #inventory menu
        print("\nInventory Menu: ")
        print("1. View Inventory")
        print("2. Search Inventory")
        print("3. Go back")
        #input
        try:
            sel = int(input("Please select an option: "))
        except ValueError:
            sel = 0
        #options
        if sel == 1:
            inventory.viewInventory(inventory.databaseName)
        elif sel == 2:
            inventory.searchInventory()
        elif sel == 3:
            break
        else:
            print("Invalid option")
def cartMenu():
    while user.loggedIn:
        #cart menu
        print("\nCart Menu: ")
        print("1. View Cart")
        print("2. Add items to Cart")
        print("3. Remove an Item from Cart")
        print("4. Check out")
        print("5. Go Back")
        try:
            sel = int(input("Please select an option: "))
        except ValueError:
            sel = 0
        #options
        if sel == 1:
            cart.viewCart(cart.datbaseName)
        elif sel == 2:
            cart.addToCart(cart.isbn)
        elif sel == 3:
            cart.removeFromCart(cart.isbn)
        elif sel == 4:
            cart.checkOut(cart.userID)
        elif sel == 5:
            break
        else:
            print("Invalid option")
while not exiting:
    startMenu()
    mainMenu()

cursor.close()
connection.close()
    
