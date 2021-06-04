# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boardingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from encoding import encoding
from decoding import decoding,check_decoded
from reportlab.pdfgen import canvas
from fpdf import FPDF

class Ui_boardingWindow(object):
    def setupUi(self, boardingWindow):
        boardingWindow.setObjectName("boardingWindow")
        boardingWindow.resize(799, 451)
        boardingWindow.setStyleSheet("background-color: rgb(30,144,255);")
        self.centralwidget = QtWidgets.QWidget(boardingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(320, 10, 161, 51))
        self.title_label.setStyleSheet("font: 87 20pt \"Segoe UI Black\";")
        self.title_label.setObjectName("title_label")
        self.UBC_label = QtWidgets.QLabel(self.centralwidget)
        self.UBC_label.setGeometry(QtCore.QRect(30, 130, 321, 31))
        self.UBC_label.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.UBC_label.setObjectName("UBC_label")

        self.dialog_label = QtWidgets.QLabel(self.centralwidget)
        self.dialog_label.setGeometry(QtCore.QRect(290, 340, 241, 51))
        self.dialog_label.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.dialog_label.setObjectName("dialog_label")




        self.UBC_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UBC_lineEdit.setGeometry(QtCore.QRect(410, 130, 351, 31))
        self.UBC_lineEdit.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.UBC_lineEdit.setObjectName("UBC_lineEdit")

        self.tickets_btn = QtWidgets.QPushButton(self.centralwidget)
        self.tickets_btn.setGeometry(QtCore.QRect(310, 230, 161, 41))
        self.tickets_btn.setStyleSheet("background-color: rgb(135,206,250);\n"
"font: 87 10pt \"Arial Black\";")
        self.tickets_btn.setObjectName("tickets_btn")
        self.tickets_btn.clicked.connect(self.showdetails)


        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(340, 310, 93, 28))
        self.exit_btn.setStyleSheet("background-color: rgb(255,99,71);\n"
"font: 87 10pt \"Arial Black\";")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(boardingWindow.close)

        boardingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(boardingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        boardingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(boardingWindow)
        self.statusbar.setObjectName("statusbar")
        boardingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(boardingWindow)
        QtCore.QMetaObject.connectSlotsByName(boardingWindow)

    def retranslateUi(self, boardingWindow):
        _translate = QtCore.QCoreApplication.translate
        boardingWindow.setWindowTitle(_translate("boardingWindow", "boardingWindow"))
        self.title_label.setText(_translate("boardingWindow", "Boarding"))
        self.UBC_label.setText(_translate("boardingWindow", "Unique Boarding Code"))
        self.tickets_btn.setText(_translate("boardingWindow", "Get Tickets"))
        self.exit_btn.setText(_translate("boardingWindow", "Exit"))

    def showdetails(self):
        text = self.UBC_lineEdit.text()
        strprint,matched = check_decoded(text)
        # print(strprint)
        if matched == False:
            self.dialog_label.setText("Wrong code")
        else:
            self.dialog_label.setText("Tickets generated")
            textLines = ["Flight ID: " + strprint[5], "Name: " + strprint[0], "Gender: " + strprint[1],
                         "Date: " + strprint[2], "From: " + strprint[3], "To: " + strprint[4]]
            filename = 'tickets.pdf'
            document_title = 'Tickets'
            subtitle = 'Happy Journey'
            image = 'qrcode.jpg'
            pdf = canvas.Canvas(filename)
            pdf.setTitle(document_title)

            pdf.setFont('Helvetica-Bold', 26)
            pdf.drawCentredString(300, 770, document_title)

            pdf.setFont('Helvetica-Bold', 20)
            pdf.drawCentredString(300, 750, subtitle)

            text = pdf.beginText(90, 680)
            text.setFont("Helvetica", 18)
            for line in textLines:
                text.textLine(line)

            pdf.drawText(text)

            pdf.drawInlineImage(image, 350, 600, 100, 100)

            pdf.save()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_boardingWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

