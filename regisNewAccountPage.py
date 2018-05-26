# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regisNewAccountPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import firebase
import subYearInfoPage
import subYearInfoPageHead
import firstLoginPage

class Ui_Regis(object):
    def setupUi(self, Form):
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        Form.setObjectName("Form")
        Form.resize(1271, 823)
        self.Form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 1051, 191))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fNameEntry = QtWidgets.QLineEdit(Form)
        self.fNameEntry.setGeometry(QtCore.QRect(520, 260, 501, 61))
        self.fNameEntry.setObjectName("fNameEntry")
        self.fNameLabel = QtWidgets.QLabel(Form)
        self.fNameLabel.setGeometry(QtCore.QRect(240, 250, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fNameLabel.setFont(font)
        self.fNameLabel.setObjectName("fNameLabel")
        self.lNameLabel = QtWidgets.QLabel(Form)
        self.lNameLabel.setGeometry(QtCore.QRect(240, 360, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lNameLabel.setFont(font)
        self.lNameLabel.setObjectName("lNameLabel")
        self.lNameEntry = QtWidgets.QLineEdit(Form)
        self.lNameEntry.setGeometry(QtCore.QRect(520, 370, 501, 61))
        self.lNameEntry.setObjectName("lNameEntry")
        self.uNameLabel = QtWidgets.QLabel(Form)
        self.uNameLabel.setGeometry(QtCore.QRect(240, 470, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.uNameLabel.setFont(font)
        self.uNameLabel.setObjectName("uNameLabel")
        self.uNameEntry = QtWidgets.QLineEdit(Form)
        self.uNameEntry.setGeometry(QtCore.QRect(520, 480, 501, 61))
        self.uNameEntry.setObjectName("uNameEntry")
        self.roleLabel = QtWidgets.QLabel(Form)
        self.roleLabel.setGeometry(QtCore.QRect(240, 580, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.roleLabel.setFont(font)
        self.roleLabel.setObjectName("roleLabel")
        self.roleEntry = QtWidgets.QComboBox(Form)
        self.roleEntry.setGeometry(QtCore.QRect(520, 590, 231, 61))
        self.roleEntry.setObjectName("roleEntry")
        self.roleEntry.addItem("")
        self.roleEntry.addItem("")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(1030, 710, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.next)

        self.logOutButton = QtWidgets.QPushButton(Form)
        self.logOutButton.setGeometry(QtCore.QRect(150, 710, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.logOutButton.setFont(font)
        self.logOutButton.setObjectName("logOutButton")
        self.logOutButton.setText("logout")
        self.logOutButton.clicked.connect(self.logOut)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def reOpen(self, Form,first,last,username,role):
        self.first = first
        self.last = last
        self.username = username
        self.role = role
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        Form.setObjectName("Form")
        Form.resize(1271, 823)
        self.Form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 1051, 191))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fNameEntry = QtWidgets.QLineEdit(Form)
        self.fNameEntry.setGeometry(QtCore.QRect(520, 260, 501, 61))
        self.fNameEntry.setObjectName("fNameEntry")
        self.fNameLabel = QtWidgets.QLabel(Form)
        self.fNameLabel.setGeometry(QtCore.QRect(240, 250, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fNameLabel.setFont(font)
        self.fNameLabel.setObjectName("fNameLabel")
        self.lNameLabel = QtWidgets.QLabel(Form)
        self.lNameLabel.setGeometry(QtCore.QRect(240, 360, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lNameLabel.setFont(font)
        self.lNameLabel.setObjectName("lNameLabel")
        self.lNameEntry = QtWidgets.QLineEdit(Form)
        self.lNameEntry.setGeometry(QtCore.QRect(520, 370, 501, 61))
        self.lNameEntry.setObjectName("lNameEntry")
        self.uNameLabel = QtWidgets.QLabel(Form)
        self.uNameLabel.setGeometry(QtCore.QRect(240, 470, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.uNameLabel.setFont(font)
        self.uNameLabel.setObjectName("uNameLabel")
        self.uNameEntry = QtWidgets.QLineEdit(Form)
        self.uNameEntry.setGeometry(QtCore.QRect(520, 480, 501, 61))
        self.uNameEntry.setObjectName("uNameEntry")
        self.roleLabel = QtWidgets.QLabel(Form)
        self.roleLabel.setGeometry(QtCore.QRect(240, 580, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.roleLabel.setFont(font)
        self.roleLabel.setObjectName("roleLabel")
        self.roleEntry = QtWidgets.QComboBox(Form)
        self.roleEntry.setGeometry(QtCore.QRect(520, 590, 231, 61))
        self.roleEntry.setObjectName("roleEntry")
        self.roleEntry.addItem("")
        self.roleEntry.addItem("")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(1030, 710, 191, 71))

        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.next)

        self.logOutButton = QtWidgets.QPushButton(Form)
        self.logOutButton.setGeometry(QtCore.QRect(150, 710, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.logOutButton.setFont(font)
        self.logOutButton.setObjectName("logOutButton")
        self.logOutButton.setText("logout")
        self.logOutButton.clicked.connect(self.logOut)

        self.fNameEntry.setText(self.first)
        self.lNameEntry.setText(self.last)
        self.uNameEntry.setText(self.username)
        self.roleEntry.setCurrentText(self.role)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Register A New Account"))
        self.fNameLabel.setText(_translate("Form", "First Name: "))
        self.lNameLabel.setText(_translate("Form", "Last Name: "))
        self.uNameLabel.setText(_translate("Form", "Username:"))
        self.roleLabel.setText(_translate("Form", "Role:"))
        self.roleEntry.setItemText(0, _translate("Form", "Teacher"))
        self.roleEntry.setItemText(1, _translate("Form", "Head Teacher"))
        self.nextButton.setText(_translate("Form", "Next"))


    def next(self):
        if self.validate():
            print("yes")
            first = self.fNameEntry.text()
            last = self.lNameEntry.text()
            username = self.uNameEntry.text()
            role = self.roleEntry.currentText()

            if(role == "Teacher"):
                self.window = QtWidgets.QMainWindow()
                self.ui = subYearInfoPage.Ui_SubYear()
                self.ui.setupUi(self.window, first, last, username, role)
                self.Form.hide()
                self.window.show()

            if(role == "Head Teacher"):
                self.window = QtWidgets.QMainWindow()
                self.ui = subYearInfoPageHead.Ui_Form()
                self.ui.setupUi(self.window,first,last,username,role)
                self.Form.hide()
                self.window.show()


    def validate(self):
        if self.fNameEntry.text() == '':
            self.showError(2)
            return 0
        elif self.lNameEntry.text() == '':
            self.showError(3)
            return 0
        elif self.uNameEntry.text() == '':
            self.showError(4)
            return 0

        self.username = self.uNameEntry.text()
        self.teachers = self.db.get('/Teachers', None)

        if(self.username in self.teachers):
            self.generateUsername()
            return 0

        return 1

    def showError(self,i):

        if (i == 2):
            temp = 'Please enter first name'
        elif (i== 3):
            temp = 'Please enter last name'
        elif i == 4:
            temp = 'Please enter username'

        dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText(temp)
        layout.addWidget(label)

        confirm_button = QPushButton('Close')
        confirm_button.clicked.connect(dialog.close)
        layout.addWidget(confirm_button)
        dialog.setLayout(layout)
        dialog.show()


    def generateUsername(self):
        count = 1
        while (self.username in self.teachers):
            count += 1
            self.username = self.fNameEntry.text()+self.lNameEntry.text()[0:count]

        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("This is suggestion username " + self.username)
        layout.addWidget(label)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.ConfirmPassword)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()


    def ConfirmPassword(self):
        self.uNameEntry.setText(self.username)
        self.dialog.close()

    def logOut(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = firstLoginPage.Ui_Login()
        self.ui.setupUi(self.window)
        self.Form.hide()
        self.window.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Regis()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

