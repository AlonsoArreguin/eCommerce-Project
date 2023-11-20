from InventoryClass import Inventory, connection, cursor
from UserClass import User
from CartClass import Cart

#create database tables if they don't exist here
connection.execute('''
    CREATE TABLE IF NOT EXISTS inventory(
        ISBN integer PRIMARY KEY,
        Title text NOT NULL, 
        Author text NOT NULL,
        Genre text NOT NULL,
        Pages integer NOT NULL,
        ReleaseDate date NOT NULL
        Stock integer NOT NULL)
        ''')
connection.execute('''
    CREATE TABLE IF NOT EXISTS user(
        UserID integer PRIMARY KEY,
        Email text NOT NULL,
        Password text NOT NULL,
        FirstName text NOT NULL,
        LastName text NOT NULL,
        Address text NOT NULL,
        City text NOT NULL,
        State text NOT NULL,
        Zip integer NOT NULL,
        Payment text NOT NULL)
        ''')
connection.execute('''
    CREATE TABLE IF NOT EXITS cart(
        UserID integer,
        ISBN integer,
        Quantity integer NOT NULL,
        FOREIGN KEY(userID) REFERENCES user(userID)
        FOREIGN KEY(isbn) REFERENCES inventory(isbn))
        ''')
#create sample datasets here if they do not exist
inventoryData =[
    ('123456789', 'The Hunger Games', 'Suzanne Collins', 'Fiction', 300, '2008-09-14', 30),
    ('987654321', 'The Woman in Me', 'Britney Spears', 'Memoir', 287, '2023-10-22', 60),
    ('483753920', 'Im Glad My Mom Died', 'Jenette McCurdy', 'Memoir', 290, '2022-10-19', 20)
]

cursor.executemany('INSERT INTO Inventory VALUES (?, ?, ?, ?, ?, ?, ?), inventoryData')
connection.commit()
    
