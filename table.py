#!/usr/bin/python
import sys


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)


except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# A few global variables which will be used in the handshaking with C++
salesmanData = []
dataComplete = False

# The orders class, this will display all the orders that currently need to be processed
class Ui_Orders(QtGui.QTableWidget):

    # Init function calls superclass and sets it self up
    def __init__(self):
        super(Ui_Orders,self).__init__()
        self.setupTable()

    # Sets the table up, adding columns header etc
    def setupTable(self):

        # Adding some columns and initial row
        self.setColumnCount(5)

        # Set the style of the grid
        self.setGridStyle(Qt.DashLine)

        self.horizontalHeader().setStretchLastSection(True)

        # Name the columns
        self.setHorizontalHeaderLabels(['Name', 'Address', 'Postcode', 'Coordinates', 'Products'])

    def sendDataForCalculation(self):
        
        # Declare our intensions to modify the global salesmanData variable
        global salesmanData
        global dataComplete

        # For each of the rows
        for i in range(0,self.rowCount()):
            xy = self.item(i,3).text()
            xy = xy.split(',')

            salesmanData.append([i, float(xy[0]), float(xy[1])])

        dataComplete = True

    def addRow(self, data):
        rows = self.rowCount()
        self.insertRow(rows)
        rows = self.rowCount()

        for i in range(0,4):
            self.setItem(rows-1,i, QTableWidgetItem(data[i]))

# Order form class used to get input from user and is eventually used to display that data
class Ui_OrderForm(QtGui.QWidget):

    def __init__(self):
        super(Ui_OrderForm,self).__init__()
        self.setupForm()

    def setupForm(self):

        # Use a VBox layout
        self.formLayout = QtGui.QVBoxLayout()

        # Title 
        title = QtGui.QLabel("New Order")
        title.setAlignment(Qt.AlignHCenter)
        self.formLayout.addWidget(title)

        # Name
        self.nameField = QtGui.QLineEdit()
        self.formLayout.addWidget(QtGui.QLabel("Name: "),1)
        self.formLayout.addWidget(self.nameField)

        # Address
        self.addressField = QtGui.QLineEdit()
        self.formLayout.addWidget(QtGui.QLabel("Address: "),1)
        self.formLayout.addWidget(self.addressField)

        # Postcode
        self.postcodeField = QtGui.QLineEdit()
        self.formLayout.addWidget(QtGui.QLabel("Postcode: "),1)
        self.formLayout.addWidget(self.postcodeField)

        # Coordinates
        self.coordLayout = QtGui.QHBoxLayout()
        self.coordX = QtGui.QLineEdit()
        self.coordY = QtGui.QLineEdit()

        self.coordX.setMaximumWidth(75)
        self.coordX.setPlaceholderText("X: ")

        self.coordY.setMaximumWidth(75)
        self.coordY.setPlaceholderText("Y: ")

        self.formLayout.addWidget(QtGui.QLabel("Coordinates: "),1)
        self.coordLayout.addWidget(self.coordX)
        self.coordLayout.addWidget(self.coordY)
        self.coordLayout.addStretch(1)
        self.formLayout.addLayout(self.coordLayout)

        # Compress everything together
        self.formLayout.addStretch(6)

        # Set the layout
        self.setLayout(self.formLayout)

    def getData(self):

        # Create an empty list to store the data in
        data = []

        # Name
        name = self.formLayout.itemAt(2).widget()
        data.append(name.text())

         # Address
        address = self.formLayout.itemAt(4).widget()
        data.append(address.text())

        # Post code
        postcode = self.formLayout.itemAt(6).widget()
        data.append(postcode.text())

        # Coordinates
        Xcoord = self.formLayout.itemAt(8).layout().itemAt(0).widget()
        Ycoord = self.formLayout.itemAt(8).layout().itemAt(1).widget()
        coords = "%s,%s" % (Xcoord.text(), Ycoord.text())
        data.append(coords)

        return data

    def clearFields(self):
        for i in 2,4,6:
            self.formLayout.itemAt(i).widget().clear()

        self.formLayout.itemAt(8).layout().itemAt(0).widget().clear()
        self.formLayout.itemAt(8).layout().itemAt(1).widget().clear()

# The main UI class everything is controlled here
class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUI()

    def setupUI(self):

        # Window title and dimensions
        self.setWindowTitle('Axiom Enterprises - Route Logistics')
        self.setGeometry(200,200,1500,750)

        # Widgets
        self.orderWidget = Ui_Orders()
        self.formWidget = Ui_OrderForm()
        self.centreWidget = QtGui.QWidget()
        self.centreLayout = QtGui.QHBoxLayout()

        # Centre Widget layout
        self.centreLayout.addWidget(self.orderWidget, 2)
        self.centreLayout.addWidget(self.formWidget, 1)

        # Passing everything to the main window
        self.centreWidget.setLayout(self.centreLayout)
        self.setCentralWidget(self.centreWidget)

        # Bottom dock
        bottomDock = QtGui.QDockWidget()
        bottomDockWidget = QtGui.QWidget()
        buttonLayout = QtGui.QHBoxLayout()

        buttonLayout.addStretch(1)

        # Add new order button
        self.addOrderButton = QtGui.QPushButton("Add Order")
        self.addOrderButton.clicked.connect(self.addOrder)

        self.calculateRouteButton = QtGui.QPushButton("Calculate Route")
        self.calculateRouteButton.clicked.connect(self.calcRoute)

        buttonLayout.addWidget(self.calculateRouteButton)
        buttonLayout.addWidget(self.addOrderButton)

        bottomDockWidget.setLayout(buttonLayout)
        bottomDock.setWidget(bottomDockWidget)
        bottomDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottomDock)

    def calcRoute(self):
        self.orderWidget.sendDataForCalculation()
        print salesmanData

    def addOrder(self):
        data = self.formWidget.getData()
        self.formWidget.clearFields()
        self.orderWidget.addRow(data)

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, '!!!WARNING!!!',
            "Are you sure to quit? All data will be lost", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
 
def main():
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec_()
    return True;

if __name__ == '__main__':
    main()
    
    
