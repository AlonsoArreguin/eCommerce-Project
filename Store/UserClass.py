class User:
    def __init__(self, databaseName="", tableName="", loggedIn=False, userID=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = loggedIn
        self.userID = userID

    def login(self):

        pass

    def logout(self):

        pass

    def viewAccountInformation(self):

        pass

    def createAccount(self):

        pass

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID
