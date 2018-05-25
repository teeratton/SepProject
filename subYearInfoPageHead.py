# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subYearInfoPageHead.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(1269, 825)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(500, 30, 521, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(200, 180, 900, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.scienceCheck = QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scienceCheck.setFont(font)
        self.scienceCheck.setObjectName("scienceCheck")
        self.scienceCheck.setGeometry(QtCore.QRect(670, 400, 251, 61))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.mathCheck = QRadioButton(self.groupBox)
        self.mathCheck.setFont(font)
        self.mathCheck.setObjectName("mathCheck")
        self.mathCheck.setGeometry(QtCore.QRect(130, 80, 231, 61))



        font = QtGui.QFont()
        font.setPointSize(16)
        self.thaiCheck = QRadioButton(self.groupBox)
        self.thaiCheck.setFont(font)
        self.thaiCheck.setObjectName("thaiCheck")
        self.thaiCheck.setGeometry(QtCore.QRect(670, 230, 121, 61))


        font = QtGui.QFont()
        font.setPointSize(16)
        self.engCheck = QRadioButton(self.groupBox)
        self.engCheck.setFont(font)
        self.engCheck.setObjectName("engCheck")
        self.engCheck.setGeometry(QtCore.QRect(130, 230, 141, 61))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.socialCheck = QRadioButton(self.groupBox)
        self.socialCheck.setGeometry(QtCore.QRect(670, 80, 221, 61))
        self.socialCheck.setFont(font)
        self.socialCheck.setObjectName("socialCheck")

        self.geoCheck = QRadioButton(self.groupBox)
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
        self.backButton.setGeometry(QtCore.QRect(50, 730, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Subject Information"))
        self.scienceCheck.setText(_translate("Form", "Science"))
        self.mathCheck.setText(_translate("Form", "Mathematics"))
        self.thaiCheck.setText(_translate("Form", "Thai"))
        self.engCheck.setText(_translate("Form", "English"))
        self.socialCheck.setText(_translate("Form", "Social Studies"))
        self.geoCheck.setText(_translate("Form", "Geography"))
        self.doneButton.setText(_translate("Form", "Done"))
        self.backButton.setText(_translate("Form", "Back"))

    def done(self):
        if (self.readData() == True):
            self.printSummary()
        else:
            self.showError()

    def readData(self):
        count = 1
        length = len(self.buttonCheck)
        self.subjects.clear()
        for i in range(length):
            if self.buttonCheck[i].isChecked():
                if self.entryList[i].text() != "":
                    years = self.entryList[i].text()
                    for x in years.split(','):
                        if self.isValid(x):
                            self.subjects.update({"sub" + str(count): self.subjectName[i] + x})
                            count += 1
                        else:
                            return False
                else:
                    return False
            else:
                if self.entryList[i].text() != "":
                    return False

        return True

    def printSummary(self):
        self.password = self.generatePassword()
        print(self.subjects)
        print(self.password)

        self.t = teacher(self.first, self.last, self.username, self.password, self.subjects)

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
        lusername.setText(
            "Username : " + self.username + "\n" + "Password : " + self.password + "\n" + "First name: " + self.first +
            "\n" + "Last name: " + self.last + "\n" + "Role: " + self.role + "\n" + "Subject: " + subjectList)
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

    def showError(self):
        dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("Invalid input")
        layout.addWidget(label)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(dialog.close)
        layout.addWidget(confirm_button)
        dialog.setLayout(layout)

        dialog.show()


    def Confirm(self):
        self.db.put('Teachers', self.username, self.teacher)
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
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

