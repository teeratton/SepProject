# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstLoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from firebase import firebase
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        Form.setObjectName("Form")
        Form.resize(1274, 826)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 90, 721, 141))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.unameEntry = QtWidgets.QLineEdit(Form)
        self.unameEntry.setGeometry(QtCore.QRect(530, 350, 401, 51))
        self.unameEntry.setObjectName("unameEntry")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 340, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 450, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pwordEntry = QtWidgets.QLineEdit(Form)
        self.pwordEntry.setGeometry(QtCore.QRect(530, 470, 401, 51))
        self.pwordEntry.setObjectName("pwordEntry")
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(480, 620, 271, 71))
        self.loginButton.clicked.connect(self.login)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Exam Bank"))
        self.label_2.setText(_translate("Form", "Username:"))
        self.label_3.setText(_translate("Form", "Password:"))
        self.loginButton.setText(_translate("Form", "Login"))

    def login(self):
        print("login")
        username = self.unameEntry.text()
        password = self.pwordEntry.text()
        usernames = self.db.get('/Login',None)
        if(username in usernames):
            id = self.db.get('/Login/' + username, None)
            if (id.get('password') == password):
                print("get in")
            else:
                print("incorrect password")


    def checkUsername(self,username):
        teachers = self.db.get('/Teachers',None)
        if (username in teachers):
            print("username is already exist")
            return 0
        return 1





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

