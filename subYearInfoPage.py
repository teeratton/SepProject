# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subYearInfoPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random
import string
from firebase import firebase
import regisNewAccountPage
from teacher import teacher



class Ui_SubYear(object):
    def setupUi(self, Form,first,last,username,role):
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.subjects = {}
        self.first = first
        self.last = last
        self.username = username
        self.role = role
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(1269, 825)
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(270, 20, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scienceCheck = QtWidgets.QCheckBox(Form)
        self.scienceCheck.setGeometry(QtCore.QRect(670, 400, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scienceCheck.setFont(font)
        self.scienceCheck.setObjectName("scienceCheck")
        self.mathCheck = QtWidgets.QCheckBox(Form)
        self.mathCheck.setGeometry(QtCore.QRect(110, 610, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mathCheck.setFont(font)
        self.mathCheck.setObjectName("mathCheck")
        self.thaiCheck = QtWidgets.QCheckBox(Form)
        self.thaiCheck.setGeometry(QtCore.QRect(680, 200, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.thaiCheck.setFont(font)
        self.thaiCheck.setObjectName("thaiCheck")
        self.engCheck = QtWidgets.QCheckBox(Form)
        self.engCheck.setGeometry(QtCore.QRect(130, 200, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.engCheck.setFont(font)
        self.engCheck.setObjectName("engCheck")
        self.socialCheck = QtWidgets.QCheckBox(Form)
        self.socialCheck.setGeometry(QtCore.QRect(670, 610, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.socialCheck.setFont(font)
        self.socialCheck.setObjectName("socialCheck")
        self.geoCheck = QtWidgets.QCheckBox(Form)
        self.geoCheck.setGeometry(QtCore.QRect(120, 400, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.geoCheck.setFont(font)
        self.geoCheck.setObjectName("geoCheck")

        self.doneButton = QtWidgets.QPushButton(Form)
        self.doneButton.setGeometry(QtCore.QRect(1090, 730, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneButton.setFont(font)
        self.doneButton.setObjectName("doneButton")

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(120, 730, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")

        self.geoEntry = QtWidgets.QLineEdit(Form)
        self.geoEntry.setGeometry(QtCore.QRect(370, 400, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.geoEntry.setFont(font)
        self.geoEntry.setObjectName("geoEntry")
        self.mathEntry = QtWidgets.QLineEdit(Form)
        self.mathEntry.setGeometry(QtCore.QRect(370, 610, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mathEntry.setFont(font)
        self.mathEntry.setObjectName("mathEntry")
        self.engEntry = QtWidgets.QLineEdit(Form)
        self.engEntry.setGeometry(QtCore.QRect(370, 200, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.engEntry.setFont(font)
        self.engEntry.setObjectName("engEntry")
        self.thaiEntry = QtWidgets.QLineEdit(Form)
        self.thaiEntry.setGeometry(QtCore.QRect(940, 200, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thaiEntry.setFont(font)
        self.thaiEntry.setObjectName("thaiEntry")
        self.scienceEntry = QtWidgets.QLineEdit(Form)
        self.scienceEntry.setGeometry(QtCore.QRect(940, 400, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scienceEntry.setFont(font)
        self.scienceEntry.setObjectName("scienceEntry")
        self.socialEntry = QtWidgets.QLineEdit(Form)
        self.socialEntry.setGeometry(QtCore.QRect(940, 610, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.socialEntry.setFont(font)
        self.socialEntry.setObjectName("socialEntry")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, hisEntry):
        _translate = QtCore.QCoreApplication.translate
        hisEntry.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Subject and Year Information"))
        self.scienceCheck.setText(_translate("Form", "Science"))
        self.mathCheck.setText(_translate("Form", "Mathematics"))
        self.thaiCheck.setText(_translate("Form", "Thai"))
        self.engCheck.setText(_translate("Form", "English"))
        self.socialCheck.setText(_translate("Form", "Social Studies"))
        self.geoCheck.setText(_translate("Form", "Geography"))
        self.doneButton.setText(_translate("Form", "Done"))
        self.backButton.setText(_translate("Form","Back"))
        self.doneButton.clicked.connect(self.done)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = regisNewAccountPage.Ui_Regis()
        self.ui.reOpen(self.window, self.first, self.last, self.username, self.role)
        self.Form.hide()
        self.window.show()
    
    def done(self):
        count = 1
        if(self.mathCheck.isChecked()):
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub"+str(count):"Mathematic"+x})
                count+=1


        if (self.scienceCheck.isChecked()):
            years = self.scienceEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub"+str(count):"Science"+x})
                count+=1

        if (self.thaiCheck.isChecked()):
            years = self.thaiEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Thai" + x})
                count += 1

        if (self.engCheck.isChecked()):
            years = self.engEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "English" + x})
                count += 1

        if (self.socialCheck.isChecked()):
            years = self.socialEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Social Studies" + x})
                count += 1

        if (self.geoCheck.isChecked()):
            years = self.geoEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Geography" + x})
                count += 1
        else:
            print("please enter subject")

        self.password = self.generatePassword()
        print(self.subjects)
        print(self.password)

        self.t = teacher(self.first,self.last,self.username,self.password,self.subjects)

        self.teacher = {'first': self.t.first, 'last': self.t.last, 'password': self.t.password, 'role': self.role,
                    'subjects': self.t.subjects}

        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        subjectList = ""

        for i in self.subjects:
            if i == "sub1":
                subjectList += self.subjects.get(i)
            else:
                subjectList += ", " + self.subjects.get(i)


        lusername = QLabel(self.Form)
        lusername.setText("Username : " + self.username + "\n" + "Password : " + self.password + "\n" + "First name: " + self.first +
                          "\n" + "Last name: " + self.last + "\n" + "Role: " + self.role + "\n" + "Subject: " + subjectList )
        layout.addWidget(lusername)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.Confirm)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()


    def Confirm(self):
        self.db.put('Teachers',self.username,self.teacher)
        self.dialog.close()



    def generatePassword(self):
        passWord = ""
        for i in range(8):
            passWord += random.choice(string.ascii_letters + string.digits)
        return passWord


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_SubYear()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

