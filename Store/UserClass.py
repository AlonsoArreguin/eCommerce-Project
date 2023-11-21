import sqlite3
from InventoryClass import connection, cursor 
import sys

class User:
    def __init__(self, databaseName="", tableName="", loggedIn=False, userID=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = loggedIn
        self.userID = userID


    def login(self):
       if not self.loggedIn:
            userid = input("Enter your UserID: ")
            password = input("Enter your password: ")

            try:
                cursor.execute("SELECT * FROM user WHERE userid=? AND password=?".format(self.tableName), (userid, password,))
                row = cursor.fetchone()

                if row is not None:
                    self.loggedIn = True
                    self.userID = userid
                    print("Login successful. Welcome, {}!".format(userid))
                    return True
                else:
                    print("Login failed. Invalid username or password.")
                    return False

            except sqlite3.Error as e:
                print("Error during login:", e)
                return False
       else:
            print("User already logged in.")
            return False


    def logout(self):

        if self.loggedIn:
            print("Logout successful. Goodbye, {}!".format(self.userID))
            self.loggedIn = False
            self.userID = ""
            return True
        else:
            print("User not logged in.")
            return False

    def viewAccountInformation(self):

        if self.loggedIn:
            try:
                cursor.execute("SELECT Username FROM {} WHERE UserID=?".format(self.tableName), (self.userID,))
                row = cursor.fetchone()

                if row is not None:
                    username = row[0]
                    print("Account information for username: ", username)
                else:
                    print("Username not found.")
            except sqlite3.Error as e:
                print("Error fetching account information:", e)
        else:
            print("User not logged in. Please login to view account information.")


    def createAccount(self):

        if not self.loggedIn:
            new_userid = input("Enter UserID for new account: ")
            new_email = input("Enter Email: ")
            new_password = input("Enter Password for new account: ")
            new_firstname = input("Enter First Name: ")
            new_lastname = input("Enter Last Name: ")
            new_address = input("Enter Address: ")
            new_city = input("Enter City: ")
            new_state = input("Enter State: ")
            new_zip = input("Enter ZIP: ")
            new_payment = input("Enter Payment Method: ")

            try:
                # Check if the UserID already exists
                cursor.execute("SELECT userid FROM user WHERE userid=?".format(self.tableName), (new_userid,))
                existing_userid = cursor.fetchone()

                if existing_userid:
                    print("UserID already in use. Cannot create a new account.")
                else:
                    # Insert the new account if the username is not in use
                    cursor.execute("INSERT INTO user (userid, email, password, firstname, lastname, address, city, state, zip, payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(self.tableName), (new_userid,new_email,new_password,new_firstname,new_lastname,new_address,new_city,new_state,new_zip,new_payment))
                    connection.commit()
                    print("Account for {} created successfully!".format(new_firstname))

            except sqlite3.Error as e:
                print("Error creating account: ", e)
        else:
            print("User already logged in. Cannot create a new account.")


    def getLoggedIn(self):

        return self.loggedIn

    def getUserID(self):

        return self.userID