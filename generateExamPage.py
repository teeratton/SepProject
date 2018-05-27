# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generateExamPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from teacher import teacher
from firebase import firebase
import random
import math

class Ui_Form(object):
    def setupUi(self, Form,t):
        Form.setObjectName("Form")
        Form.resize(1265, 842)
        self.Form = Form
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.t = t
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(650, 210, 271, 51))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 210, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 350, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.previewButton = QtWidgets.QPushButton(Form)
        self.previewButton.setGeometry(QtCore.QRect(1020, 750, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.previewButton.setFont(font)
        self.previewButton.setObjectName("previewButton")
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(40, 750, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 0, 471, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.numberEntry = QtWidgets.QLineEdit(Form)
        self.numberEntry.setGeometry(QtCore.QRect(650, 340, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numberEntry.setFont(font)
        self.numberEntry.setText("")
        self.numberEntry.setObjectName("numberEntry")
        self.previewButton.clicked.connect(self.generate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        for x in self.t.getSubjects() :
            self.comboBox.addItem(self.t.getSubjects().get(x))

        self.questions = self.db.get('/ApprovedQuestions',None)
        self.q = []
        #print(self.questions)


        #print(self.q)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Select A Course ID:"))
        self.label_3.setText(_translate("Form", "Enter Number of Questions in Exam:"))
        self.previewButton.setText(_translate("Form", "Preview Exam"))
        self.backButton.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Generate An Exam"))

    def generate(self):
        self.q.clear()
        self.selectQuestions = []
        self.quesNum = int(self.numberEntry.text())
        self.selectSubId = self.comboBox.currentText()
        for x in self.questions:
            s = self.questions.get(x).get('subId')
            if(s == self.selectSubId):
                self.q.append(self.questions.get(x))

        if(self.quesNum >= len(self.q)):
            self.showError()

        else:
            self.separate = math.ceil(self.quesNum / 2)
            self.randomNum = []


            self.easy = []
            self.normal = []
            self.hard = []

            for i in range(len(self.q)):
                if self.q[i].get('level') == 'Normal':
                    self.normal.append(self.q[i])
                if self.q[i].get('level') == 'Easy':
                    self.easy.append(self.q[i])
                if self.q[i].get('level') == 'Hard':
                    self.hard.append(self.q[i])
            count = 0
            temp = []
            while (count < self.separate):
                data = random.randint(0, len(self.normal) - 1)
                if(data not in temp):
                    self.selectQuestions.append(self.normal[data])
                    count+=1

            remain = self.quesNum - self.separate
            remainForEasy = math.ceil(remain / 2)
            remainForHard = remain - remainForEasy

            temp = []
            count = 0

            while (count < remainForEasy):
                data = random.randint(0, len(self.easy) - 1)
                print(data)
                if (data not in temp):
                    self.selectQuestions.append(self.easy[data])
                    count += 1

            temp = []
            count = 0
            while (count < remainForHard):
                data = random.randint(0, len(self.hard) - 1)
                print(data)
                if (data not in temp):
                    self.selectQuestions.append(self.hard[data])
                    count += 1


            for i in range(len(self.selectQuestions)):
                print(self.selectQuestions[i].get('level'))

            self.selectQuestions.clear()

    def showError(self):
        dialog = QtWidgets.QDialog(self.Form)
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(self.Form)
        label.setText("Not enough questions")
        layout.addWidget(label)

        confirm_button = QtWidgets.QPushButton('Confirm')
        confirm_button.clicked.connect(dialog.close)
        layout.addWidget(confirm_button)
        dialog.setLayout(layout)

        dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

