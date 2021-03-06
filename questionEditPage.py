from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import statusSystem
import random
import string
from firebase import firebase


class Ui_Form(object):
    def setupUi(self, Form, question, t):
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.t = t
        self.selectQuestion = question
        self.quesID = self.selectQuestion.questionId
        self.courseID = self.selectQuestion.subId
        self.question = self.selectQuestion.question
        self.ansA = self.selectQuestion.ansA
        self.ansB = self.selectQuestion.ansB
        self.ansC = self.selectQuestion.ansC
        self.ansD = self.selectQuestion.ansD
        self.correctAns = self.selectQuestion.correctAns
        self.level = self.selectQuestion.level

        Form.setObjectName("Form")
        Form.resize(1265, 842)
        self.Form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, -20, 651, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 170, 271, 51))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.questionText = QtWidgets.QTextEdit(Form)
        self.questionText.setGeometry(QtCore.QRect(360, 170, 851, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.questionText.setFont(font)
        self.questionText.setObjectName("questionText")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(360, 110, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 390, 171, 351))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.aRadio = QtWidgets.QRadioButton(self.groupBox)
        self.aRadio.setGeometry(QtCore.QRect(100, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aRadio.setFont(font)
        self.aRadio.setObjectName("aRadio")
        self.bRadio = QtWidgets.QRadioButton(self.groupBox)
        self.bRadio.setGeometry(QtCore.QRect(100, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bRadio.setFont(font)
        self.bRadio.setObjectName("bRadio")
        self.cRadio = QtWidgets.QRadioButton(self.groupBox)
        self.cRadio.setGeometry(QtCore.QRect(100, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cRadio.setFont(font)
        self.cRadio.setObjectName("cRadio")
        self.dRadio = QtWidgets.QRadioButton(self.groupBox)
        self.dRadio.setGeometry(QtCore.QRect(100, 300, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dRadio.setFont(font)
        self.dRadio.setObjectName("dRadio")
        self.aText = QtWidgets.QTextEdit(Form)
        self.aText.setGeometry(QtCore.QRect(270, 430, 941, 61))
        self.aText.setObjectName("aText")
        self.bText = QtWidgets.QTextEdit(Form)
        self.bText.setGeometry(QtCore.QRect(270, 510, 941, 61))
        self.bText.setObjectName("bText")
        self.cText = QtWidgets.QTextEdit(Form)
        self.cText.setGeometry(QtCore.QRect(270, 590, 941, 61))
        self.cText.setObjectName("cText")
        self.dText = QtWidgets.QTextEdit(Form)
        self.dText.setGeometry(QtCore.QRect(270, 670, 941, 61))
        self.dText.setObjectName("dText")
        self.doneButton = QtWidgets.QPushButton(Form)
        self.doneButton.setGeometry(QtCore.QRect(1090, 760, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doneButton.setFont(font)
        self.doneButton.setObjectName("doneButton")
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(40, 760, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.questionText.setText(self.question)
        self.aText.setText(self.ansA)
        self.bText.setText(self.ansB)
        self.cText.setText(self.ansC)
        self.dText.setText(self.ansD)
        print(self.courseID)


        if (self.correctAns == "A"):
            self.aRadio.setChecked(True)
        elif (self.correctAns == "B"):
            self.bRadio.setChecked(True)
        elif (self.correctAns == "C"):
            self.cRadio.setChecked(True)
        else:
            self.dRadio.setChecked(True)

        self.doneButton.clicked.connect(self.done)
        self.backButton.clicked.connect(self.back)

        for x in self.t.getSubjects() :
            self.comboBox.addItem(self.t.getSubjects().get(x))
        index = self.comboBox.findText(self.courseID)
        self.comboBox.setCurrentIndex(index)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Upload An Exam Question"))
        self.label_2.setText(_translate("Form", "Select A Course ID:"))
        self.questionText.setHtml(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Question:"))
        self.label_4.setText(_translate("Form", "Please select the"))
        self.label_5.setText(_translate("Form", "correct answer choice."))
        self.groupBox.setTitle(_translate("Form", "Choices:"))
        self.aRadio.setText(_translate("Form", "A"))
        self.bRadio.setText(_translate("Form", "B"))
        self.cRadio.setText(_translate("Form", "C"))
        self.dRadio.setText(_translate("Form", "D"))
        self.aText.setHtml(_translate("Form", ""))
        self.bText.setHtml(_translate("Form", ""))
        self.cText.setHtml(_translate("Form", ""))
        self.dText.setHtml(_translate("Form", ""))
        self.doneButton.setText(_translate("Form", "Done"))
        self.backButton.setText(_translate("Form", "Back"))

    def validate(self):
        if self.questionText.toPlainText() == "":
            return 0
        if self.aText.toPlainText() == "" and self.bText.toPlainText() == "" and self.cText.toPlainText() == "" :
            return 0
        if (self.aText.toPlainText() != "" and self.bText.toPlainText() != "" and self.cText.toPlainText() != "") and self.dText.toPlainText() == "":
            if(self.aRadio.isChecked() or self.bRadio.isChecked() or self.cRadio.isChecked()):
                return 3
        if self.aRadio.isChecked() or self.bRadio.isChecked() or self.cRadio.isChecked() or self.dRadio.isChecked():
            if self.aText.toPlainText() != "" and self.bText.toPlainText() != "" and self.cText.toPlainText() != "" and self.dText.toPlainText() != "":
                return 1
        else:
            return 2

    def showDialog(self):
        if (self.validate() == 3):
            self.dialogException = QDialog(self.Form)
            layout = QVBoxLayout()

            label = QLabel(self.Form)
            label.setText("Are you sure you want only 3 multiple choice answer? ")
            layout.addWidget(label)

            confirm_button = QPushButton('Yes')
            confirm_button.clicked.connect(self.Confirmation)
            layout.addWidget(confirm_button)
            self.dialogException.setLayout(layout)

            close_button = QPushButton('No')
            close_button.clicked.connect(self.dialogException.close)
            layout.addWidget(close_button)
            self.dialogException.setLayout(layout)
            self.dialogException.show()
        else:
            if (self.validate() == 2):
                temp = 'Please tick correct answer'
            elif (self.validate() == 0):
                temp = 'Please fill the text box'
            else:
                temp = 'Please fill the text box'

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

    def done(self):
        if self.validate() == 1:
            self.Confirmation()
        elif self.validate() == 3:
            self.dialogException.close()
            self.Confirmation()
        else:
            self.showDialog()

    def Confirmation(self):
        self.subId = self.comboBox.currentText()
        self.question = self.questionText.toPlainText()
        self.ansA = self.aText.toPlainText()
        self.ansB = self.bText.toPlainText()
        self.ansC = self.cText.toPlainText()
        self.ansD = self.dText.toPlainText()
        if (self.aRadio.isChecked()):
            self.correctAnswer = self.aRadio.text()
        if (self.bRadio.isChecked()):
            self.correctAnswer = self.bRadio.text()
        if (self.cRadio.isChecked()):
            self.correctAnswer = self.cRadio.text()
        if (self.dRadio.isChecked()):
            self.correctAnswer = self.dRadio.text()

        # self.q = question(self.subId,self.question,self.ansA,self.ansB,self.ansC,self.ansD,self.correctAnswer,"",self.quesId,self.t.username)

        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("Do you want to upload")
        layout.addWidget(label)

        confirm_button = QPushButton('Yes')
        confirm_button.clicked.connect(self.ConfirmPassword)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()



    def ConfirmPassword(self):
        self.pendingQuestion = {'subId': self.subId, 'question': self.question, 'ansA': self.ansA, 'ansB': self.ansB,
                                'ansC': self.ansC
            , 'ansD': self.ansD, 'correctAnswer': self.correctAnswer, 'level': "", 'quesId': self.quesID,
                                'teacherUsername': self.t.username}

        self.db.put('PendingQuestions', self.quesID, self.pendingQuestion)
        self.db.delete('RejectQuestions/'+ self.quesID,None)
        self.dialog.close()
        self.successDialog()

    def successDialog(self):
        dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("The question is edited")
        layout.addWidget(label)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.back)
        layout.addWidget(confirm_button)
        dialog.setLayout(layout)
        dialog.show()

    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = statusSystem.statusSystem()
        self.ui.setupUi(self.window, self.t)
        self.Form.hide()
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

