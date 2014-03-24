#!/usr/bin/python2.7

import sys


from PyQt4 import QtCore, QtGui

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


class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUI()
    
    def setupUI(self):
        
                
        '''
        Arranges how big and where the interface on the screen will be
        '''

        
        self.setWindowTitle('Axiom Enterprises - Route Logistics')
        self.setGeometry(200,200,750,750)  # window size and location
        
    

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self) # exit process     
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit) # possible ways to exit with a shortcut

      
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')  # toolbar options
        fileMenu.addAction(exitAction)  # toolbar subsections
       
        
        # These are used to create the overall look of the screen
        mainLayout   = QtGui.QVBoxLayout()
        dataLayout = QtGui.QHBoxLayout()
        buttonLayout = QtGui.QHBoxLayout()

        # Each of These Contain the elements of the form, eg name,address etc
        formElementName = QtGui.QVBoxLayout()
        formElementAddress = QtGui.QVBoxLayout()
        formElementPostcode = QtGui.QVBoxLayout()
        formElementCoords = QtGui.QVBoxLayout()
        formElementProd1 = QtGui.QVBoxLayout()
        formElementProd2 = QtGui.QVBoxLayout()
        formElementProd3 = QtGui.QVBoxLayout()
        
        centralWidget =     QtGui.QWidget()
        """
        gridLayout.addWidget(QtGui.QLabel("Product"),2,0)
        gridLayout.addWidget(QtGui.QLabel("Quantity"),2,1)
        
        gridLayout.addWidget(QtGui.QLabel("Inspiron 15R"),3,0) # can't seem to get this above the middle of the page
        gridLayout.addWidget(QtGui.QComboBox(),3,1)
        gridLayout.addWidget(QtGui.QPushButton("Add new stock"),3,2)
        """
        formElementName.addWidget(QtGui.QLabel("Customer Name"))
        formElementName.addWidget(QtGui.QLineEdit())

        formElementAddress.addWidget(QtGui.QLabel("First line of address"))
        formElementAddress.addWidget(QtGui.QLineEdit())

        formElementPostcode.addWidget(QtGui.QLabel("Postcode"))
        formElementPostcode.addWidget(QtGui.QLineEdit())

        formElementCoords.addWidget(QtGui.QLabel("Coordinates"))
        formElementCoords.addWidget(QtGui.QLineEdit())

        formElementProd1.addWidget(QtGui.QLabel("Product 1"))
        formElementProd1.addWidget(QtGui.QComboBox())

        formElementProd1.addWidget(QtGui.QLabel("Quantity"))
        formElementProd1.addWidget(QtGui.QComboBox())

        formElementProd2.addWidget(QtGui.QLabel("Product 2"))
        formElementProd2.addWidget(QtGui.QComboBox())

        formElementProd2.addWidget(QtGui.QLabel("Quantity"))
        formElementProd2.addWidget(QtGui.QComboBox())

        formElementProd3.addWidget(QtGui.QLabel("Product 3"))
        formElementProd3.addWidget(QtGui.QComboBox())

        formElementProd3.addWidget(QtGui.QLabel("Quantity"))
        formElementProd3.addWidget(QtGui.QComboBox())

        dataLayout.addLayout(formElementName)
        dataLayout.addLayout(formElementAddress)
        dataLayout.addLayout(formElementPostcode)
        dataLayout.addLayout(formElementCoords)
        dataLayout.addLayout(formElementProd1)
        dataLayout.addLayout(formElementProd2)
        dataLayout.addLayout(formElementProd3)
        dataLayout.addWidget(QtGui.QPushButton("Add Order"))

        buttonLayout.addStretch(1)
        buttonLayout.addWidget(QtGui.QPushButton("Ok"))
        buttonLayout.addWidget(QtGui.QPushButton("cancel"))

        mainLayout.addLayout(dataLayout)
        mainLayout.addStretch(0.5)
        mainLayout.addLayout(buttonLayout)
 

        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(mainLayout)

        self.resize(750,750)       
      
        


        
       
        
    def closeEvent(self, event):
               
        reply = QtGui.QMessageBox.question(self, '!!!WARNING!!!',
            "Are you sure to quit, all data will be lost?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
  
      
          
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
    
