import sqlite3
import sys

try:
    connection = sqlite3.connect("userdatabase.db")
    print("Successful connection")
except:
    print("Failed connection")

    sys.exit()

cursor = connection.cursor()

class User:
    def __init__(self, databaseName="", tableName="", loggedIn=False, userID=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = loggedIn
        self.userID = userID


    def login(self):

        if not self.loggedIn:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            try:
                cursor.execute("SELECT * FROM {} WHERE username=? AND password=?".format(self.tableName), (username, password))
                row = cursor.fetchone()

                if row is not None:
                    self.loggedIn = True
                    self.userID = username
                    print("Login successful. Welcome, {}!".format(username))
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
                cursor.execute("SELECT username FROM {} WHERE userID=?".format(self.tableName), (self.userID,))
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
            new_username = input("Enter username for new account: ")
            new_password = input("Enter password for new account: ")

            try:
                cursor.execute("INSERT INTO {} (username, password) VALUES (?, ?)".format(self.tableName), (new_username, new_password))
                connection.commit()
                print("Account for {} created successfully!".format(new_username))
            except sqlite3.Error as e:
                print("Error creating account: ", e)


            print("Account for {} created successfully!".format(new_username))
        else:
            print("username already in used. Cannot create a new account.")

    def getLoggedIn(self):

        return self.loggedIn

    def getUserID(self):

        return self.userID
