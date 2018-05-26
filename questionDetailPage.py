# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questionDetailPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from firebase import firebase

import headTeacherPage

class Ui_Form(object):
    def setupUi(self, Form,question,ht):
        self.Form = Form
        self.ht = ht
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
        self.username = self.selectQuestion.teacherUsername
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        Form.setObjectName("Form")
        Form.resize(1267, 822)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, -30, 411, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 100, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 420, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(130, 500, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(130, 580, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(130, 660, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.questionIdLabel = QtWidgets.QLabel(Form)
        self.questionIdLabel.setGeometry(QtCore.QRect(40, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.questionIdLabel.setFont(font)
        self.questionIdLabel.setObjectName("questionIdLabel")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 270, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.rightAnswerLabel = QtWidgets.QLabel(Form)
        self.rightAnswerLabel.setGeometry(QtCore.QRect(270, 270, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rightAnswerLabel.setFont(font)
        self.rightAnswerLabel.setObjectName("rightAnswerLabel")
        self.notAppButton = QtWidgets.QPushButton(Form)
        self.notAppButton.setGeometry(QtCore.QRect(550, 740, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notAppButton.setFont(font)
        self.notAppButton.setObjectName("notAppButton")
        self.AppButton = QtWidgets.QPushButton(Form)
        self.AppButton.setGeometry(QtCore.QRect(1010, 740, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AppButton.setFont(font)
        self.AppButton.setObjectName("AppButton")
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(40, 740, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.displayQuestion = QtWidgets.QTextBrowser(Form)
        self.displayQuestion.setGeometry(QtCore.QRect(350, 150, 861, 241))
        self.displayQuestion.setObjectName("displayQuestion")
        self.ansAEntry = QtWidgets.QTextBrowser(Form)
        self.ansAEntry.setGeometry(QtCore.QRect(270, 410, 941, 61))
        self.ansAEntry.setObjectName("ansA")
        self.ansBEntry = QtWidgets.QTextBrowser(Form)
        self.ansBEntry.setGeometry(QtCore.QRect(270, 490, 941, 61))
        self.ansBEntry.setObjectName("ansB")
        self.ansCEntry = QtWidgets.QTextBrowser(Form)
        self.ansCEntry.setGeometry(QtCore.QRect(270, 570, 941, 61))
        self.ansCEntry.setObjectName("ansC")
        self.ansDEntry = QtWidgets.QTextBrowser(Form)
        self.ansDEntry.setGeometry(QtCore.QRect(270, 650, 941, 61))
        self.ansDEntry.setObjectName("ansD")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.questionIdLabel.setText(self.quesID)
        self.displayQuestion.setText(self.question)
        self.rightAnswerLabel.setText(self.correctAns)
        self.ansAEntry.setText(self.ansA)
        self.ansBEntry.setText(self.ansB)
        self.ansCEntry.setText(self.ansC)
        self.ansDEntry.setText(self.ansD)

        self.backButton.clicked.connect(self.back)
        self.AppButton.clicked.connect(self.approve)






    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Question Details"))
        self.label_3.setText(_translate("Form", "Question:"))
        self.label_2.setText(_translate("Form", "A"))
        self.label_6.setText(_translate("Form", "B"))
        self.label_7.setText(_translate("Form", "C"))
        self.label_8.setText(_translate("Form", "D"))
        self.label_9.setText(_translate("Form", "Question ID:"))
        self.questionIdLabel.setText(_translate("Form", "1122347"))
        self.label_11.setText(_translate("Form", "Correct Choice:"))
        self.rightAnswerLabel.setText(_translate("Form", "A"))
        self.notAppButton.setText(_translate("Form", "Not Approve"))
        self.AppButton.setText(_translate("Form", "Approve"))
        self.backButton.setText(_translate("Form", "Back"))
        self.displayQuestion.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ansAEntry.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

    def approve(self):
        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("Please select level of the question")
        layout.addWidget(label)

        self.comboBox = QComboBox(self.Form)
        self.comboBox.addItem("Easy")
        self.comboBox.addItem("Normal")
        self.comboBox.addItem("Hard")
        layout.addWidget(self.comboBox)
        self.dialog.setLayout(layout)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.confirmApprove)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()

    def confirmApprove(self):

        self.approvedQuestion = {'subId': self.courseID, 'question': self.question, 'ansA': self.ansA, 'ansB': self.ansB,
                                'ansC': self.ansC
            , 'ansD': self.ansD, 'correctAnswer': self.correctAns, 'level': self.comboBox.currentText(), 'quesId': self.quesID,
                                'teacherUsername': self.username}

        self.db.put('ApprovedQuestions', self.quesID, self.approvedQuestion)

        self.db.delete('PendingQuestions/'+self.quesID,None)

        self.dialog.close
        self.back()

    def reject(self):
        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("Please select level of the question")
        layout.addWidget(label)

        self.comment = QTextEdit(self.Form)
        layout.addWidget(self.comment)
        self.dialog.setLayout(layout)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.confirmRejct)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()

    def confirmReject(self):
        pass




    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = headTeacherPage.Ui_Form()
        self.ui.setupUi(self.window, self.ht)
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

