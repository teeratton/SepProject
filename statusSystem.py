# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkQuestionStatus.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from firebase import firebase
from PyQt5 import QtCore, QtGui, QtWidgets
from question import question
from PyQt5.QtWidgets import *
import teacherPage
import questionEditPage
import loginSystem

class statusSystem(object):
    def setupUi(self, Form,t):
        Form.setObjectName("Form")
        self.t = t
        self.Form=Form
        
        self.first = self.t.getFirst()
        self.last = self.t.getLast()
        self.subject = self.t.getSubjects()
        self.username = self.t.getUsername()

        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.y = 0
        self.count = 0
        self.stop = 3
        self.start = 0
        self.a = []
        
        Form.resize(1262, 819)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, -20, 751, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.firstLastLabel = QtWidgets.QLabel(Form)
        self.firstLastLabel.setGeometry(QtCore.QRect(410, 90, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.firstLastLabel.setFont(font)
        self.firstLastLabel.setObjectName("firstLastLabel")
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setGeometry(QtCore.QRect(1020, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.qInboxLabel = QtWidgets.QLabel(Form)
        self.qInboxLabel.setGeometry(QtCore.QRect(60, 90, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.qInboxLabel.setFont(font)
        self.qInboxLabel.setObjectName("qInboxLabel")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(950, 650, 181, 71))
        self.nextButton.clicked.connect(self.increment)
        self.backButton = QtWidgets.QPushButton(self.Form)
        self.backButton.setGeometry(QtCore.QRect(750, 650, 181, 71))
        self.backButton.clicked.connect(self.decrement)

        self.logoutButton.clicked.connect(self.logOut)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.logoutButton.setText("Mainmenu")

        self.nextButton.raise_()
        self.nextButton.hide()
        self.backButton.raise_()
        self.backButton.hide()


        self.firstLastLabel.setText(self.first + " " + self.last)
        self.questions = self.db.get('/PendingQuestions', None)
        self.rejects = self.db.get('/RejectQuestions',None)

        self.q = []
        if(len(self.rejects) != 0):
            for x in self.rejects:
                tu = (self.rejects.get(x).get('teacherUsername'))
                if (self.username == tu):
                    self.q.append(self.rejects.get(x))

        if (len(self.q) != 0):
            print("KAO WEII")
            self.showSomething()
        else:
            self.nextButton.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Check Exam Questions Status"))
        self.firstLastLabel.setText(_translate("Form", "display teacher full name"))
        self.logoutButton.setText(_translate("Form", "Log Out"))
        self.qInboxLabel.setText(_translate("Form", "Question Inbox:"))
        self.backButton.setText(_translate("Form", "Back"))
        self.nextButton.setText(_translate("Form", "Next"))


    def retranslateUi2(self,Form):
        _translate = QtCore.QCoreApplication.translate
        self.quesLabel.setText(_translate("Form", "Question ID:"))
        self.courseIdLabel.setText(_translate("Form", "Course ID:"))
        self.statusLabel.setText(_translate("Form", "Status:"))
        self.commentLabel.setText(_translate("Form", "Comment:"))
        self.editButton.setText(_translate("Form", "Edit "))
        self.deleteButton.setText(_translate("Form", "Delete"))
            
    def increment(self):
            self.backButton.show()
            for x in self.a:
                x.hide()

            self.start += 3
            self.stop += 3

            self.y = 0
            self.a.clear()
            self.showSomething()

    def decrement(self):
        for x in self.a:
            x.hide()

        if (self.start != 0):
            self.start -= 3
            self.stop -= 3

        self.y = 0
        self.a.clear()

        self.backButton.show()
        self.nextButton.show()
        self.showSomething()

    def showSomething(self):
        for i in range(self.start, self.stop, 1):
            self.quesID = self.q[i].get('quesId')
            self.courseID = self.q[i].get('subId')
            self.question = self.q[i].get('question')
            self.ansA = self.q[i].get('ansA')
            self.ansB = self.q[i].get('ansB')
            self.ansC = self.q[i].get('ansC')
            self.ansD = self.q[i].get('ansD')
            self.correctAns = self.q[i].get('correctAnswer')
            self.level = self.q[i].get('level')
            self.username = self.q[i].get('teacherUsername')
            self.comment = self.q[i].get('comment')

            self.selectQuestion = question(self.quesID, self.courseID, self.question, self.ansA,
                        self.ansB, self.ansC, self.ansD, self.correctAns, self.level, self.username)

            font = QtGui.QFont()
            font.setPointSize(14)

            self.quesLabel = QtWidgets.QLabel(self.Form)
            self.quesLabel.setGeometry(QtCore.QRect(190, 210 + self.y, 161, 51))
            self.quesLabel.setFont(font)
            self.quesLabel.setObjectName("quesLabel")

            self.courseIdLabel = QtWidgets.QLabel(self.Form)
            self.courseIdLabel.setGeometry(QtCore.QRect(190, 240 + self.y, 131, 51))
            self.courseIdLabel.setFont(font)
            self.courseIdLabel.setObjectName("courseIdLabel")

            self.statusLabel = QtWidgets.QLabel(self.Form)
            self.statusLabel.setGeometry(QtCore.QRect(190, 270 + self.y, 161,51))
            self.statusLabel.setFont(font)
            self.statusLabel.setObjectName("statusLabel")

            self.commentLabel = QtWidgets.QLabel(self.Form)
            self.commentLabel.setGeometry(QtCore.QRect(450, 210 + self.y, 161,51))
            self.commentLabel.setFont(font)
            self.commentLabel.setObjectName("commentLabel")

            self.displayQuesId = QtWidgets.QLabel(self.Form)
            self.displayQuesId.setGeometry(QtCore.QRect(320, 210 + self.y, 131, 51))
            self.displayQuesId.setFont(font)
            self.displayQuesId.setObjectName("displayQuesId")

            self.displayCourseId = QtWidgets.QLabel(self.Form)
            self.displayCourseId.setGeometry(QtCore.QRect(320, 240 + self.y, 241, 51))
            self.displayCourseId.setFont(font)
            self.displayCourseId.setObjectName("displayCourseId")

            self.displayStatus = QtWidgets.QLabel(self.Form)
            self.displayStatus.setGeometry(QtCore.QRect(320, 270 + self.y, 241, 51))
            self.displayStatus.setFont(font)
            self.displayStatus.setObjectName("displayCourseId")

            self.editButton = QtWidgets.QPushButton(self.Form)
            self.editButton.setGeometry(QtCore.QRect(980, 225 + self.y, 131,61))
            self.editButton.setFont(font)

            self.deleteButton = QtWidgets.QPushButton(self.Form)
            self.deleteButton.setGeometry(QtCore.QRect(980, 275 + self.y, 131, 61))
            self.deleteButton.setFont(font)

            self.displayComment = QtWidgets.QTextBrowser(self.Form)
            self.displayComment.setGeometry(QtCore.QRect(530,230 + self.y,431, 100))
            self.displayComment.setObjectName("displayComment")

            self.a.append(self.quesLabel)
            self.a.append(self.displayQuesId)
            self.a.append(self.displayCourseId)
            self.a.append(self.courseIdLabel)
            self.a.append(self.statusLabel)
            self.a.append(self.displayStatus)
            self.a.append(self.commentLabel)
            self.a.append(self.deleteButton)
            self.a.append(self.nextButton)
            self.a.append(self.displayComment)
            self.a.append(self.editButton)

            for x in self.a:
                x.show()

            self.editButton.clicked.connect(lambda checked, arg = self.selectQuestion: self.edit(arg))
            self.deleteButton.clicked.connect(lambda checked, arg = self.selectQuestion: self.reject(arg))

            self.quesLabel.raise_()
            self.displayQuesId.raise_()
            self.courseIdLabel.raise_()
            self.displayCourseId.raise_()
            self.statusLabel.raise_()
            self.displayStatus.raise_()
            self.commentLabel.raise_()
            self.deleteButton.raise_()
            self.displayComment.raise_()
            self.editButton.raise_()
            self.nextButton.raise_()

            self.retranslateUi2(self.Form)

            self.displayQuesId.setText(self.quesID)
            self.displayCourseId.setText(self.courseID)
            self.displayStatus.setText("REJECTED")
            self.displayComment.setText(self.comment)
  
            self.y += 150

            if self.start == 0:
                self.backButton.hide()

            if i == self.stop - len(self.q):
                break

            if i == len(self.q) - 1:
                self.nextButton.hide()
                break

    def reject(self, x):
        self.newX = x.getQuestionId()
        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        label = QLabel(self.Form)
        label.setText("Are you sure you want to delete this question?")
        layout.addWidget(label)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.helper)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()

    def helper(self):
        self.confirmReject(self.newX)

    def confirmReject(self, x):
        self.tempStatus = 0
        self.db.delete('/RejectQuestions/' + x, None)
        self.dialog.close()

        self.dialog = QtWidgets.QDialog(self.Form)
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(self.Form)
        label.setText('The question is deleted')
        layout.addWidget(label)

        confirm_button = QtWidgets.QPushButton('Confirm')
        confirm_button.clicked.connect(self.backAgain)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)
        self.dialog.show()

    def backAgain(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = statusSystem()
        self.ui.setupUi(self.window, self.t)
        self.Form.hide()
        self.window.show()


    def edit(self,x):
        self.window = QtWidgets.QMainWindow()
        self.ui = questionEditPage.Ui_Form()
        self.ui.setupUi(self.window, x, self.t)
        self.Form.hide()
        self.window.show()


    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = teacherPage.Ui_Form()
        self.ui.setupUi(self.window, self.t)
        self.Form.hide()
        self.window.show()

    def logOut(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = teacherPage.Ui_Form()
        self.ui.setupUi(self.window,self.t)
        self.Form.hide()
        self.window.show()

    def successDialog(self):
        if (self.tempStatus == 0):
            text = "The question is approved"
        elif (self.tempStatus == 1):
            text = "The question is rejected"

        dialog = QtWidgets.QDialog(self.Form)
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(self.Form)
        label.setText(text)
        layout.addWidget(label)

        confirm_button = QtWidgets.QPushButton('Confirm')
        confirm_button.clicked.connect(self.back)
        layout.addWidget(confirm_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = statusSystem()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

