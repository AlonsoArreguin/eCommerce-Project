# connect to sqlite and db file and invenory
import sqlite3
import sys
from InventoryClass import Inventory
## attempts to connect to database
try:
    connection = sqlite3.connect("inventorydatabase.db")
    print("Successful connection")
except:
    print("Failed connection.")

try:
    con = sqlite3.connect("cartdatabase.db")
    print("Successful connection")
except:
    print("Failed connection")
    ## exits the program if unsuccessful
    sys.exit()

cursor = connection.cursor()
cur = con.cursor()

class Cart:
    datbaseName = str
    tableName = str
    userID = str
    isbn = str

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
def addToCart(userID, isbn):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Inventory SET Stock = Stock + 1 WHERE isbn = ?", (isbn, ))
    connection.commit()
    if cursor.rowcount > 0:
        print(f"ISBN {isbn} item added  successfully.") #no need for else here since it will always be true


def removeFromCart(userID, isbn): #do the same thing as add but instead subtract
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Inventory SET Stock = Stock - 1 WHERE isbn = ?", (isbn, ))
    connection.commit()
    if cursor.rowcount > 0:
        print(f"ISBN {isbn} item removed successfully.")
    else:
        print(f"{isbn} not found in the cart. Failed to remove from cart.")
def checkOut(userID):
    inventory = Inventory(databaseName = "inventorydatabase.db", tableName = "isbn")
    cursor = connection.cursor()
    cursor.execute ("SELECT isbn FROM inventory WHERE userID = ?", (userID,))
    rows = cursor.fetchall()
    if rows: 
        for item in rows:
            inventory.decreaseStock(userID)
        #remove all items from user's cart after checkout
        cursor.execute("DELETE FROM Cart WHERE userID = ?",(userID,))
        connection.commit()
        print(f"(userID) has checked out. Cart items removed and stock updated.")   
    else:
        print("Cart is empty.")     