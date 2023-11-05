# connect to sqlite and db file
import sqlite3
import sys
## attempts to connect to database
try:
    connection = sqlite3.connect("inventorydatabase.db")
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
    
    

    def __init__(self, databaseName="", tableName="", isbn=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.isbn = isbn
        
    def viewInventory(self, databaseName):
        self.databaseName = databaseName
        cursor = connection.cursor()
        cursor.execute ("SELECT * FROM inventory")
        rows = cursor.fetchall()
        if rows:
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
        if rows:
            #Displays specific title user inputted
            for row in rows:
                print(f"ISBN: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}, Pages: {row[4]}, Release Date: {row[5]}, Stock: {row[6]}")
        else:
            print(f"The title '{title}' was not found in the inventory.")
        
#Test variables for view inventory   
#inventory =  Inventory(databaseName = "inventorydatabase.db")
#inventory.viewInventory(databaseName = "inventorydatabase.db")
#Test variables for search inventory
#inventory = Inventory(databaseName = "inventorydatabase.db")
#inventory.searchInventory()
cursor.close()
connection.close()
    
