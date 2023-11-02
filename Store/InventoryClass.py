# connect to sqlite and db file
import sqlite3


#Inventory Class
class Inventory:
    databaseName = str
    tableName = str
    isbn = str
    
    

    def __init__(self, databaseName="", tableName="", isbn=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.isbn = isbn
        
    
    
    
