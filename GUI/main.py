from PyQt5 import QtCore, QtGui, QtWidgets
from customer2 import Ui_customerselection
from EmpLoginWindow import Ui_EmpLoginWindow

class Ui_MainWindow(object):

    def opencustselectionwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_customerselection()
        self.ui.setupUi(self.window)
        self.window.show()

    def openemplogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EmpLoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 449)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/Desktop/main_img.jpg);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(100, 20, 491, 41))
        self.titlelabel.setStyleSheet("color: rgb(255, 255, 255);\n""font: 97 italic 25pt \"Segoe UI Black\";\n""color: rgb(0, 0, 0);")
        self.titlelabel.setObjectName("titlelabel")

        self.EmpPB = QtWidgets.QPushButton(self.centralwidget)
        self.EmpPB.setGeometry(QtCore.QRect(230, 160, 191, 51))
        self.EmpPB.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 87 12pt \"Arial Black\";")
        self.EmpPB.setObjectName("EmpPB")
        self.EmpPB.clicked.connect(self.openemplogin)
        # self.EmpPB.clicked.connect(MainWindow.close)


        self.CustPB = QtWidgets.QPushButton(self.centralwidget)
        self.CustPB.setGeometry(QtCore.QRect(230, 250, 191, 51))
        self.CustPB.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 87 12pt \"Arial Black\";")
        self.CustPB.setObjectName("CustPB")
        self.CustPB.clicked.connect(self.opencustselectionwindow)
        # self.CustPB.clicked.connect(MainWindow.close)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titlelabel.setText(_translate("MainWindow", "SPD FLIGHT TRAVELS"))
        self.EmpPB.setText(_translate("MainWindow", "Employee"))
        self.CustPB.setText(_translate("MainWindow", "Customer"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

