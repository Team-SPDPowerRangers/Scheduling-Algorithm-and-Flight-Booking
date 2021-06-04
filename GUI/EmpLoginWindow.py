from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from EmpMainWindow import Ui_EmpMainWindow
class Ui_EmpLoginWindow(object):

    def setupUi(self, EmpLoginWindow):
        EmpLoginWindow.setObjectName("EmpLoginWindow")
        EmpLoginWindow.resize(545, 600)
        EmpLoginWindow.setStyleSheet("background-color: rgb(70,130,180);\n""")
        self.centralwidget = QtWidgets.QWidget(EmpLoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(220, 10, 121, 61))
        self.title_label.setStyleSheet("font: 87 24pt \"Segoe UI Black\";")
        self.title_label.setObjectName("title_label")

        self.ID_label = QtWidgets.QLabel(self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(30, 180, 181, 31))
        self.ID_label.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.ID_label.setObjectName("ID_label")

        self.ID_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_lineEdit.setGeometry(QtCore.QRect(260, 181, 231, 31))
        self.ID_lineEdit.setStyleSheet("font: 12pt \"Arial\";\n""background-color: rgb(255, 255, 255);")
        self.ID_lineEdit.setObjectName("ID_lineEdit")

        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(30, 280, 141, 21))
        self.pass_label.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.pass_label.setObjectName("pass_label")

        self.pass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_lineEdit.setGeometry(QtCore.QRect(260, 270, 231, 31))
        self.pass_lineEdit.setStyleSheet("font: 12pt \"Arial\";\n""background-color: rgb(255, 255, 255);")
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.pass_lineEdit.setEchoMode(QLineEdit.Password)

        self.Dialog_label = QtWidgets.QLabel(self.centralwidget)
        self.Dialog_label.setGeometry(QtCore.QRect(180,100,241,31))
        self.Dialog_label.setStyleSheet("font: 14pt \"Arial\";\n""color: rgb(255, 255, 255);")
        self.Dialog_label.setObjectName("Dialog_label")

        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(230, 400, 111, 41))
        self.login_btn.setStyleSheet("background-color: rgb(192,192,192);\n""font: 87 12pt \"Arial Black\";")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.check)


        EmpLoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EmpLoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 26))
        self.menubar.setObjectName("menubar")
        EmpLoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EmpLoginWindow)
        self.statusbar.setObjectName("statusbar")
        EmpLoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EmpLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(EmpLoginWindow)

    def retranslateUi(self, EmpLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        EmpLoginWindow.setWindowTitle(_translate("EmpLoginWindow", "EmpLoginWindow"))
        self.title_label.setText(_translate("EmpLoginWindow", "Login"))
        self.ID_label.setText(_translate("EmpLoginWindow", "Employee ID"))
        self.pass_label.setText(_translate("EmpLoginWindow", "Password"))
        self.login_btn.setText(_translate("EmpLoginWindow", "Login"))


    def check(self):
        ID=self.ID_lineEdit.text()
        password =self.pass_lineEdit.text()
        if ID == "AIE19002" and password  == "adn":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_EmpMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            # EmpLoginWindow.close()
            return True

        else:
            self.Dialog_label.setText("Invalid Credentials")
            return False



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmpLoginWindow = QtWidgets.QMainWindow()
    ui = Ui_EmpLoginWindow()
    ui.setupUi(EmpLoginWindow)
    EmpLoginWindow.show()
    sys.exit(app.exec_())

