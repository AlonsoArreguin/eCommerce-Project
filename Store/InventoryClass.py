# connect to sqlite and db file
import sqlite3
import sys
## attempts to connect to database
try:
    connection = sqlite3.connect("project.db")
    print("Successful connection")
except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

cursor = connection.cursor()

#Inventory Class
class Inventory:
    databaseName = str
    tableName = str
    isbn = str
    author = str
    title = str
    genre = str
    pages = int
    releasedate = int
    stock = int

    
    

    def __init__(self, databaseName="", tableName="", isbn=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.isbn = isbn
        #setters and getters
    def getDatabaseName(self):
        return self.databaseName
    def setDatabaseName(self, databaseName):
        self.databaseName = databaseName
    def getTableName(self):
        return self.tableName
    def setTableName(self, tableName):
        self.tableName = tableName
    def viewInventory(self, databaseName):
        self.databaseName = databaseName
        cursor = connection.cursor()
        cursor.execute ("SELECT * FROM inventory")
        rows = cursor.fetchall()
        if rows:
            print("\n---------------------------------")
            print("|         INVENTORY             |")
            print("|       Viewing all books       |")
            print("---------------------------------\n")
            print(f"--- Showing {len(rows)} of {len(rows)} Products ---")
            #Displays all items in the inventory
            for row in rows:
                print(f"ISBN: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}, Pages: {row[4]}, Release Date: {row[5]}, Stock: {row[6]}")        
        else:
            print("Inventory is empty.")
    def searchInventory(self):
        title =  input("Enter title to search: ")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM inventory WHERE Title LIKE ?", (f"%{title}%",))
        rows = cursor.fetchall()
        print(f"----- You searched for \"{title}\": -----")
        print(f"----- Showing {len(rows)} of {len(rows)} Products -----")
        if rows:
            #Displays specific title user inputted
            for row in rows:
                print(f"ISBN: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}, Pages: {row[4]}, Release Date: {row[5]}, Stock: {row[6]}")
        else:
            print(f"'{title}' was not found in the inventory.")
    def decreaseStock(self, isbn):
        self.isbn = isbn
        isbn = input("Enter ISBN to search: ")
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Inventory SET Stock = Stock - 1 WHERE isbn = ?", (isbn, ))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"ISBN {isbn} stock decreased successfully.")
        else:
            print(f"{isbn} not found in the inventory. Failed to decrease the stock.")
    



    
