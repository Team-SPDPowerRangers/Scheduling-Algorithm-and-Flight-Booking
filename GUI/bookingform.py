# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookingform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ast
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from encoding import encoding

class Ui_Bookingform(object):

    details_list =[]

    # def openmainwindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()



    def setupUi(self, Bookingform):
        Bookingform.setObjectName("Bookingform")
        Bookingform.resize(751, 856)
        Bookingform.setStyleSheet("background-color: rgb(135,206,250);")
        self.centralwidget = QtWidgets.QWidget(Bookingform)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(100, 0, 561, 61))
        self.title_label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
        self.title_label.setObjectName("title_label")

        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.name_label.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")

        self.name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_lineEdit.setGeometry(QtCore.QRect(20, 130, 231, 31))
        self.name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_lineEdit.setObjectName("name_lineEdit")

        self.mobile_label = QtWidgets.QLabel(self.centralwidget)
        self.mobile_label.setGeometry(QtCore.QRect(20, 210, 101, 31))
        self.mobile_label.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.mobile_label.setObjectName("mobile_label")

        self.mobile_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile_lineEdit.setGeometry(QtCore.QRect(20, 270, 231, 31))
        self.mobile_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mobile_lineEdit.setObjectName("mobile_lineEdit")

        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(400, 80, 121, 31))
        self.gender_label.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.gender_label.setObjectName("gender_label")
        self.male_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.male_radioButton.setGeometry(QtCore.QRect(400, 130, 111, 31))
        self.male_radioButton.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.male_radioButton.setObjectName("male_radioButton")
        self.female_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.female_radioButton.setGeometry(QtCore.QRect(520, 130, 121, 31))
        self.female_radioButton.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.female_radioButton.setObjectName("female_radioButton")

        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setGeometry(QtCore.QRect(570, 660, 141, 31))
        self.submit_pushButton.setStyleSheet("background-color: rgb(170, 170, 255);\n""font: 87 10pt \"Arial Black\";\n""")
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.submit_pushButton.clicked.connect(self.list_to_file)

        self.viewcode_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewcode_pushButton.setGeometry(QtCore.QRect(400, 660, 141, 31))
        self.viewcode_pushButton.setStyleSheet("background-color: rgb(170, 170, 255);\n""font: 87 10pt \"Arial Black\";\n""")
        self.viewcode_pushButton.setObjectName("viewcode_pushButton")
        # self.viewcode_pushButton.clicked.connect(self.list_to_file)
        self.viewcode_pushButton.clicked.connect(self.showcode)

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(610, 730, 93, 28))
        self.exit_btn.setStyleSheet("font: 87 12pt \"Arial Black\";\n""background-color: rgb(255,127,80);")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(Bookingform.close)

        self.dept_label = QtWidgets.QLabel(self.centralwidget)
        self.dept_label.setGeometry(QtCore.QRect(20, 470, 241, 41))
        self.dept_label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 15pt \"Arial Black\";\n""")
        self.dept_label.setObjectName("dept_label")

        self.FromcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.FromcomboBox.setGeometry(QtCore.QRect(20, 390, 251, 31))
        self.FromcomboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FromcomboBox.setObjectName("FromcomboBox")
        self.fromlabel = QtWidgets.QLabel(self.centralwidget)
        self.fromlabel.setGeometry(QtCore.QRect(20, 340, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)

        self.fromlabel.setFont(font)
        self.fromlabel.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 15pt \"Arial Black\";\n""")
        self.fromlabel.setObjectName("fromlabel")

        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(400, 340, 241, 51))
        self.to_label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 15pt \"Arial Black\";\n""")
        self.to_label.setObjectName("to_label")

        self.TocomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TocomboBox.setGeometry(QtCore.QRect(400, 390, 251, 31))
        self.TocomboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TocomboBox.setObjectName("TomcomboBox")

        self.mm_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.mm_cbox.setGeometry(QtCore.QRect(90, 510, 75, 30))
        self.mm_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mm_cbox.setObjectName("mm_cbox")

        self.dd_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.dd_cbox.setGeometry(QtCore.QRect(20, 510, 75, 30))
        self.dd_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dd_cbox.setObjectName("dd_cbox")

        self.yy_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.yy_cbox.setGeometry(QtCore.QRect(160, 510, 75, 30))
        self.yy_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.yy_cbox.setObjectName("yy_cbox")


        # items = self.txt_to_list("temp.txt")
        # list_from = []
        # list_to = []
        # for i in items:
        #     list_from.append(i[0])
        #     list_to.append(i[1])

        a = self.txt_to_dict()
        list_from = []
        list_to = []
        for i, v in a.items():
            for j in range(len(v)):
                if v[j][0] not in list_from:
                    list_from.append(v[j][0])
                if v[j][1] not in list_to:
                    list_to.append(v[j][1])

        final_list_from = set(list_from)
        final_list_to = set(list_to)
        self.FromcomboBox.addItems(list(final_list_from))
        self.TocomboBox.addItems(list(final_list_to))

        dates = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '31']
        self.dd_cbox.addItems(dates)
        months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.mm_cbox.addItems(months)

        years = ['2021']
        self.yy_cbox.addItems(years)

        departure_date = self.dd_cbox.currentText()+"/"+self.mm_cbox.currentText()+"/"+self.yy_cbox.currentText()
        temp_list = [self.name_lineEdit.text(),'gender',self.mobile_lineEdit.text(),departure_date,self.FromcomboBox.currentText(),self.TocomboBox.currentText()]

        self.dialog_label = QtWidgets.QLabel(self.centralwidget)
        self.dialog_label.setGeometry(QtCore.QRect(230, 580, 351, 35))
        self.dialog_label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 12pt \"Arial Black\";\n""")
        self.dialog_label.setText("")
        self.dialog_label.setObjectName("dialog_label")
        self.dialog_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.code_label = QtWidgets.QLabel(self.centralwidget)
        self.code_label.setGeometry(QtCore.QRect(20, 780, 551, 31))
        self.code_label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 12pt \"Arial Black\";\n""")
        self.code_label.setText("")
        self.code_label.setObjectName("code_label")
        self.code_label.setTextInteractionFlags(Qt.TextSelectableByMouse)


        Bookingform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bookingform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 26))
        self.menubar.setObjectName("menubar")
        Bookingform.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bookingform)
        self.statusbar.setObjectName("statusbar")
        Bookingform.setStatusBar(self.statusbar)

        self.retranslateUi(Bookingform)
        QtCore.QMetaObject.connectSlotsByName(Bookingform)

    def retranslateUi(self, Bookingform):
        _translate = QtCore.QCoreApplication.translate
        Bookingform.setWindowTitle(_translate("Bookingform", "Bookingform"))
        self.title_label.setText(_translate("Bookingform", "FLIGHT TICKET RESERVATION"))
        self.name_label.setText(_translate("Bookingform", "Name"))
        self.mobile_label.setText(_translate("Bookingform", "Mobile no."))
        self.gender_label.setText(_translate("Bookingform", "Gender"))
        self.male_radioButton.setText(_translate("Bookingform", "Male"))
        self.female_radioButton.setText(_translate("Bookingform", "Female"))
        self.submit_pushButton.setText(_translate("Bookingform", "Submit"))
        self.viewcode_pushButton.setText(_translate("Bookingform", "View Code"))
        self.exit_btn.setText(_translate("Bookingform", "Exit"))
        self.dept_label.setText(_translate("Bookingform", "Departure"))
        self.fromlabel.setText(_translate("Bookingform", "From"))
        self.to_label.setText(_translate("Bookingform", "To"))


    def list_to_file(self):
        passenger_name = self.name_lineEdit.text()
        passenger_gender = ''
        if self.male_radioButton.isChecked():
            passenger_gender = 'male'
        elif self.female_radioButton.isChecked():
            passenger_gender = 'female'
        else:
            passenger_gender = ''
        dd_Departure = self.dd_cbox.currentText()
        mm_Departure = self.mm_cbox.currentText()
        yy_Departure = self.dd_cbox.currentText()
        from_place = self.FromcomboBox.currentText()
        to_place = self.TocomboBox.currentText()
        mnumber = self.mobile_lineEdit.text()
        val = [from_place,to_place]

        def get_key(dict, val):
            for key, value in dict.items():

                    if val in value:
                        return key
                    else:
                        return " "


        a = self.txt_to_dict()
        flight_name = get_key(a,val)
        if passenger_name == '' or passenger_gender == "" or dd_Departure == '' or yy_Departure == '' or mm_Departure == '' or from_place == '' or to_place == '' or mnumber == '' or len(mnumber)!=10:
            self.dialog_label.setText("Please fill all the details correctly")
        elif flight_name == " ":
            self.dialog_label.setText("Not available")
        else:
            departure_date = self.dd_cbox.currentText() + "/" + self.mm_cbox.currentText() + "/" + self.yy_cbox.currentText()
            temp_list = [self.name_lineEdit.text(), passenger_gender, self.mobile_lineEdit.text(), departure_date,
                         self.FromcomboBox.currentText(), self.TocomboBox.currentText(),flight_name]
            self.dialog_label.setText(" ")
            self.details_list.append(temp_list)
            list_outfile = self.details_list
            f = open('passenger_detials.txt', 'a')
            for i in list_outfile:
                lines = ''
                for j in i:
                    lines = lines + j + ' '
                lines = lines + '\n'
                f.writelines(lines)
            f.close()




    def showcode(self):
        if self.dialog_label.text() == " ":
            phone_num = self.mobile_lineEdit.text()
            temp, coarray = encoding(phone_num)
            self.code_label.setText(temp)
        else :
            self.code_label.setText("cant generate code..")




    def txt_to_dict(file):
        file = "trips_to_schedule.txt"
        scheduled_flights = {}
        with open(file) as f:
            lines = f.read().splitlines()
            for line in lines:
                if ':' in line:
                    key, value = line.split(':')
                    check = ast.literal_eval(value)
                    scheduled_flights[key] = check
        return scheduled_flights


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Bookingform()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

