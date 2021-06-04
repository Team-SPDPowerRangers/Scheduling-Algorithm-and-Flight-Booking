from bookingform import Ui_Bookingform
from PyQt5 import QtCore, QtGui, QtWidgets
from boardingWindow import Ui_boardingWindow


class Ui_customerselection(object):

    def openbookingwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Bookingform()
        self.ui.setupUi(self.window)
        self.window.show()
    def openboardingwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_boardingWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, customerselectionWindow):
        customerselectionWindow.setObjectName("customerselectionWindow")
        customerselectionWindow.resize(566, 350)
        customerselectionWindow.setStyleSheet("background-color: rgb(142, 193, 255);")
        self.centralwidget = QtWidgets.QWidget(customerselectionWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bookingPB = QtWidgets.QPushButton(self.centralwidget)
        self.bookingPB.setGeometry(QtCore.QRect(200, 80, 161, 51))
        self.bookingPB.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 87 12pt \"Arial Black\";")
        self.bookingPB.setObjectName("bookingPB")
        self.bookingPB.clicked.connect(self.openbookingwindow)
        self.bookingPB.clicked.connect(customerselectionWindow.close)

        self.boarPB = QtWidgets.QPushButton(self.centralwidget)
        self.boarPB.setGeometry(QtCore.QRect(200, 180, 161, 51))
        self.boarPB.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 87 12pt \"Arial Black\";")
        self.boarPB.setObjectName("boarPB")
        self.boarPB.clicked.connect(self.openboardingwindow)

        customerselectionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(customerselectionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 26))
        self.menubar.setObjectName("menubar")
        customerselectionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(customerselectionWindow)
        self.statusbar.setObjectName("statusbar")
        customerselectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(customerselectionWindow)
        QtCore.QMetaObject.connectSlotsByName(customerselectionWindow)

    def retranslateUi(self, customerselectionWindow):
        _translate = QtCore.QCoreApplication.translate
        customerselectionWindow.setWindowTitle(_translate("customerselectionWindow", "customerselectionWindow"))
        self.bookingPB.setText(_translate("customerselectionWindow", "Booking"))
        self.boarPB.setText(_translate("customerselectionWindow", "Boarding"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customerselectionWindow = QtWidgets.QMainWindow()
    ui = Ui_customerselection()
    ui.setupUi(customerselectionWindow)
    customerselectionWindow.show()
    sys.exit(app.exec_())

