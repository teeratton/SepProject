from firebase import firebase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import registerSystem
import teacherPage
from teacher import teacher
from headTeacher import headTeacher
import approveRejectSystem

class loginSystem(object):
    def setupUi(self, Form):
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(1274, 826)
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
        usernames = self.db.get('/Teachers',None)
        if(username in usernames):
            id = self.db.get('/Teachers/' + username, None)
            if (id.get('password') == password):
                if(id.get('role') == "Admin"):
                    self.window = QtWidgets.QMainWindow()
                    self.ui = registerSystem.registerSystem()
                    self.ui.setupUi(self.window)
                    self.Form.hide()
                    self.window.show()

                if(id.get('role') == "Teacher"):
                    self.t = teacher(id.get('first'),id.get('last'),username,id.get('password'),id.get('subjects'))
                    self.window = QtWidgets.QMainWindow()
                    self.ui = teacherPage.Ui_Form()
                    self.ui.setupUi(self.window,self.t)
                    self.Form.hide()
                    self.window.show()

                if(id.get('role') == "Head Teacher"):
                    self.ht = headTeacher(id.get('first'), id.get('last'),username,id.get('password'),id.get('subject'))
                    self.window = QtWidgets.QMainWindow()
                    self.ui = approveRejectSystem.approveRejectSystem()
                    self.ui.setupUi(self.window, self.ht)
                    self.Form.hide()
                    self.window.show()




            else:
                dialog = QDialog(self.Form)
                layout = QVBoxLayout()

                label = QLabel(self.Form)
                label.setText("Incorrect password")
                layout.addWidget(label)

                close_button = QPushButton('Close')
                close_button.clicked.connect(dialog.close)
                layout.addWidget(close_button)
                dialog.setLayout(layout)

                dialog.show()

                print("incorrect password")
        else:
            dialog = QDialog(self.Form)
            layout = QVBoxLayout()

            label = QLabel(self.Form)
            label.setText("username is not exist")
            layout.addWidget(label)

            close_button = QPushButton('Close')
            close_button.clicked.connect(dialog.close)
            layout.addWidget(close_button)
            dialog.setLayout(layout)

            dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = loginSystem()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

