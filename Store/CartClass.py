# connect to sqlite and db file and invenory
import sqlite3
import sys
from InventoryClass import Inventory, connection, cursor


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
        cursor.execute ("SELECT * FROM cart")
        rows = cursor.fetchall()
        if rows:
            print("\n---------------------------------")
            print("|             Cart              |")
            print("|       Viewing all books       |")
            print("---------------------------------\n")
            print(f"--- Showing {len(rows)} of {len(rows)} Products ---")
            #Displays all items in the cart
            for row in rows:
                print(f"ISBN: {row[1]}, Title: {row[2]}, Author: {row[3]}, Genre: {row[4]}, Pages: {row[5]}, Release Date: {row[6]}, Stock: {row[7]}")        
        else:
            print("Cart is empty.")
    def addToCart(userID, isbn):
        userID.isbn = isbn
        isbn = input("Enter ISBN to search: ")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO cart (isbn, title, author, genre, pages, releasedate, stock) SELECT isbn, title, author, genre, pages, releasedate, stock FROM inventory WHERE ISBN = ?", (isbn))
        cursor.execute(f"UPDATE cart SET stock = 1 where isbn = ?", (isbn))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"ISBN {isbn} item added  successfully.") #no need for else here since it will always be true


    def removeFromCart(userID, isbn): #do the same thing as add but instead subtract
        userID.isbn = isbn
        isbn = input("Enter ISBN to search: ")
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM cart WHERE isbn = ?", (isbn, ))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"ISBN {isbn} item removed successfully.")
        else:
            print(f"{isbn} not found in the cart. Failed to remove from cart.")
    def checkOut(userID):
        inventory = Inventory(databaseName = "inventorydatabase.db", tableName = "isbn")
        cursor = connection.cursor()
        cursor.execute ("SELECT * FROM cart")
        rows = cursor.fetchall()
        if rows: 
            for item in rows:
                cursor.execute(f"UPDATE Inventory SET Stock = Stock - 1 WHERE isbn = {item[1]}")
                connection.commit()
            #remove all items from user's cart after checkout
            cursor.execute(f"DELETE FROM cart")
            connection.commit()
            print(f"(userID) has checked out. Cart items removed and stock updated.")   
        else:
            print("Cart is empty.")     