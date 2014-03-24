#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

success = 0

class Ui_LoginScreen(QtGui.QWidget):

    def __init__(self):
        super(Ui_LoginScreen, self).__init__()
        self.initUI()

    def initUI(self):

        # Window title and dimensions
        self.setWindowTitle('Axiom Enterprises - Route Logistics - Login')
        self.setGeometry(200,200,500,250)

        # Layout
        self.layout = QtGui.QVBoxLayout()
        buttonLayout = QtGui.QHBoxLayout()

        # Items
        self.layout.addStretch(1)
        name =  QtGui.QLineEdit()
        name.setPlaceholderText("Username: ")
        name.setMaximumWidth(200)
        name.returnPressed.connect(self.attemptLogin)
        self.layout.addWidget(name)
        self.layout.addStretch(1)

        # Password Field
        password = QtGui.QLineEdit()
        password.setEchoMode(QtGui.QLineEdit.Password)
        password.setMaximumWidth(200)
        password.setPlaceholderText("Password: ")
        password.returnPressed.connect(self.attemptLogin)
        self.layout.addWidget(password)
        self.layout.addStretch(1)

        okButton = QtGui.QPushButton('OK')
        okButton.clicked.connect(self.attemptLogin)
        quitButton = QtGui.QPushButton('Quit')
        quitButton.clicked.connect(self.closeEvent)

        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(quitButton)

        self.layout.addLayout(buttonLayout)
        self.setLayout(self.layout)

    def attemptLogin(self):
        # Open the file containing the accounts
        # TODO: Make that the file is written in plain binary 
        # so that its not human readable

        source = open('data/accounts.txt', 'r')

        # Get the data from the file
        raw_data = source.read().split('\n')
        source.close()

        # Load the accounts
        accounts = []

        for i in raw_data:
            accounts.append(i.split(','))

        #print accounts

        # Get the login attempt
        name = (self.layout.itemAt(1).widget().text())
        password = (self.layout.itemAt(3).widget().text())

        # Clear the input fields
        self.layout.itemAt(1).widget().clear()
        self.layout.itemAt(3).widget().clear()

        #print name 
        #print password
        # TODO: If one of the fields are left blank show msg to user 
        # saying which one is needed and highlight it with a red border
        
        # Check to see if account exists
        accountExists = False
        accountIndex = 0
        j = 0

        for i in accounts:
            if i[0] == name:
                accountExists = True
                accountIndex = j
            j += 1
        #print accountExists
        #print accountIndex

        # If account exists check if password is correct
        if accountExists == True:
            if password == accounts[accountIndex][1]:
                print "Login Succeeded"
                self.loginResponse(0)
            else:
                print "Login Failed: Invalid Password"
                self.loginResponse(1)
        else:
            print "Login Failed: Invalid Username"
            self.loginResponse(1)

    # Function that executes the appropriate response to the login attempt
    def loginResponse(self, loginCode):
        """
        loginCode denotes the result from attemptLogin, the following numbers
        represent the following outcomes:
                0 - Succesful Login
                1 - Falied login - Incorrect username or password
                2 - Falied login - No username given
                3 - Failed login - No password given
                4 - Failed login - No Username or password given
        """
        if (loginCode == 0):
            print "Login was a success, opening UI"
            global success 
            success = 1
            self.closeEvent()
        elif(loginCode == 1):
            print "Incorrect password"
        elif(loginCode == 2):
            print "No username"
            self.layout.itemAt(0).widget().setPlaceholderText('Please enter a username')
        elif(loginCode == 3):
            print "No password"
            self.layout.itemAt(0).widget().setPlaceholderText('Please enter a password')
        elif(loginCode == 4):
            print "No username or password given"
            self.layout.itemAt(0).widget().setPlaceholderText('Please enter a password')
            self.layout.itemAt(0).widget().setPlaceholderText('Please enter a username')

    def closeEvent(self):
        QtCore.QCoreApplication.instance().quit()


def main():
#    print sys.argv

    app = QtGui.QApplication(sys.argv)

    window = Ui_LoginScreen()
    window.show()
    app.exec_()
    return [success]

if __name__=="__main__":
    main()
