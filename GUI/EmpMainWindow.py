from PyQt5 import QtCore, QtGui, QtWidgets
from flightscheduling import greedyFlightScheduling

class Ui_EmpMainWindow(object):

    # def openmainwindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    list_main = []
    def setupUi(self, EmpMainWindow):
        EmpMainWindow.setObjectName("EmpMainWindow")
        EmpMainWindow.resize(1089, 420)
        EmpMainWindow.setStyleSheet("background-color: rgb(100,149,237);")
        self.centralwidget = QtWidgets.QWidget(EmpMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(360, 0, 351, 51))
        self.title_label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
        self.title_label.setObjectName("title_label")

        self.from_label = QtWidgets.QLabel(self.centralwidget)
        self.from_label.setGeometry(QtCore.QRect(30, 100, 91, 31))
        self.from_label.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.from_label.setObjectName("from_label")

        self.from_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.from_cbox.setGeometry(QtCore.QRect(30, 140, 221, 31))
        self.from_cbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Calibri\";")
        self.from_cbox.setObjectName("from_cbox")

        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(780, 100, 91, 31))
        self.to_label.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.to_label.setObjectName("to_label")

        self.to_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.to_cbox.setGeometry(QtCore.QRect(780, 140, 221, 31))
        self.to_cbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Calibri\";")
        self.to_cbox.setObjectName("to_cbox")
        print(self.to_cbox.currentText())

#         self.duration_label = QtWidgets.QLabel(self.centralwidget)
#         self.duration_label.setGeometry(QtCore.QRect(780, 100, 151, 31))
#         self.duration_label.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
# "color: rgb(255, 255, 255);")
#         self.duration_label.setObjectName("duration_label")

#         self.hr_cbox = QtWidgets.QComboBox(self.centralwidget)
#         self.hr_cbox.setGeometry(QtCore.QRect(780, 140, 71, 31))
#         self.hr_cbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
# "font: 16pt \"Calibri\";")
#         self.hr_cbox.setObjectName("hr_cbox")
#
#         self.min_cbox = QtWidgets.QComboBox(self.centralwidget)
#         self.min_cbox.setGeometry(QtCore.QRect(850, 140, 71, 31))
#         self.min_cbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
# "font: 16pt \"Calibri\";")
#         self.min_cbox.setObjectName("min_cbox")

        from_lst = ['Hyderabad', 'Chennai', 'Bangalore', 'Delhi', 'Kolkata', 'Mumbai']
        self.from_cbox.addItems(from_lst)

        to_lst = ['Hyderabad', 'Chennai', 'Bangalore', 'Delhi', 'Kolkata', 'Mumbai']
        self.to_cbox.addItems(to_lst)


        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(460, 270, 171, 41))
        self.add_btn.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(135,206,235);")
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.loaddata)

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(492, 337, 91, 31))
        self.exit_btn.setStyleSheet("font: 87 12pt \"Arial Black\";\n""background-color: rgb(255,127,80);")
        self.exit_btn.setObjectName("exit_btn")
        # list_to_write = self.list_main
        self.exit_btn.clicked.connect(self.dict_to_txt)
        self.exit_btn.clicked.connect(EmpMainWindow.close)


        EmpMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EmpMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 26))
        self.menubar.setObjectName("menubar")
        EmpMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EmpMainWindow)
        self.statusbar.setObjectName("statusbar")
        EmpMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EmpMainWindow)
        QtCore.QMetaObject.connectSlotsByName(EmpMainWindow)

    def retranslateUi(self, EmpMainWindow):
        _translate = QtCore.QCoreApplication.translate
        EmpMainWindow.setWindowTitle(_translate("EmpMainWindow", "EmpMainWindow"))
        self.title_label.setText(_translate("EmpMainWindow", "Flights Scheduling"))
        self.from_label.setText(_translate("EmpMainWindow", "From"))
        self.to_label.setText(_translate("EmpMainWindow", "To"))
        self.add_btn.setText(_translate("EmpMainWindow", "Add Schedule"))
        self.exit_btn.setText(_translate("EmpMainWindow", "Exit"))

    def loaddata(self):
        lst_temp = [self.from_cbox.currentText(),self.to_cbox.currentText()]
        self.list_main.append(lst_temp)




    def dict_to_txt(self):
        file = "trips_to_schedule.txt"
        flight_schedules = greedyFlightScheduling(self.list_main)
        # print(flight_schedules)
        with open(file, 'w') as f:
            for key, value in flight_schedules.items():
                f.write('%s:%s \n' % (key, value))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmpMainWindow = QtWidgets.QMainWindow()
    ui = Ui_EmpMainWindow()
    ui.setupUi(EmpMainWindow)
    EmpMainWindow.show()
    sys.exit(app.exec_())

