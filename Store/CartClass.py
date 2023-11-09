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

def __init__(self, databaseName = "", tableName = ""):
    self.databaseName = databaseName
    self.tableName = tableName

def viewCart(userID = "",inventoryDatabase = ""):
    print ("hi")