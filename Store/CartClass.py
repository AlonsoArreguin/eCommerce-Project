# connect to sqlite and db file and invenory
import sqlite3
import sys
import InventoryClass
## attempts to connect to database
try:
    connection = sqlite3.connect("inventorydatabase.db")
    print("Successful connection")
except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

cursor = connection.cursor()

class Cart:
    datbaseName = str
    tableName = str
    userID = str
    ISBN = str

def __init__(self, databaseName = "", tableName = ""):
    self.databaseName = databaseName
    self.tableName = tableName

def viewCart(userID, databaseName):
     userID.databaseName = databaseName
        cursor = connection.cursor()
        cursor.execute ("SELECT * FROM inventory")
        rows = cursor.fetchall()
        if rows:
            print("\n---------------------------------")
            print("|             Cart              |")
            print("|       Viewing all books       |")
            print("---------------------------------\n")
            print(f"--- Showing {len(rows)} of {len(rows)} Products ---")
            #Displays all items in the cart
            for row in rows:
                print(f"ISBN: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}, Pages: {row[4]}, Release Date: {row[5]}, Stock: {row[6]}")        
        else:
            print("Inventory is empty.")
def addToCart(userID, ISBN):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Inventory SET Stock = Stock + 1 WHERE isbn = ?", (isbn, ))
    connection.commit()
    if cursor.rowcount > 0:
        print(f"ISBN {isbn} item added  successfully." #no need for else here since it will always be true


def removeFromCart(userID, ISBN): #do the same thing as add but instead subtract
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Inventory SET Stock = Stock - 1 WHERE isbn = ?", (isbn, ))
    connection.commit()
    if cursor.rowcount > 0:
        print(f"ISBN {isbn} item added  successfully."
     else:
        print(f"{isbn} not found in the cart. Failed to remove from cart.")
def checkOut(userID):
    cursor = connection.cursor()
    cursor.execute ("SELECT * FROM inventory")
    rows = cursor.fetchall()
    if rows:
        #continiue from here
