import sqlite3

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

            if """add authenticatio method here""":
                self.loggedIn = True
                self.userID = username
                print("Login successful. Welcome, {}!".format(username))
                return True
            else:
                print("Login failed, Invalid username or password.")
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
            print("Account information for userID: ", self.userID)
        else:
            print("User not logged in. Please login to view account inforation.")

    def createAccount(self):

        if not self.loggedIn:
            new_username = input("Enter username for new account: ")
            new_password = input("Enter password for new account: ")

            """add authentication method here"""
            print("Account for {} created successfully!".format(new_username))
        else:
            print("username already in used. Cannot create a new account.")

    def getLoggedIn(self):

        return self.loggedIn

    def getUserID(self):

        return self.userID
