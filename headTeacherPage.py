# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'headTeacherPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import firebase
from question import question
import questionDetailPage


class Ui_Form(object):
    def setupUi(self, Form, ht):
        Form.setObjectName("Form")
        self.Form = Form
        self.ht = ht
        self.first = self.ht.first
        self.last = self.ht.last
        self.username = self.ht.username
        self.subject = self.ht.subject
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.y = 0
        self.count = 0
        self.stop = 3
        self.start = 0
        self.a = []

        Form.resize(1262, 819)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, -20, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.firstLastLabel = QtWidgets.QLabel(Form)
        self.firstLastLabel.setGeometry(QtCore.QRect(510, 90, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.firstLastLabel.setFont(font)
        self.firstLastLabel.setObjectName("firstLastLabel")
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setGeometry(QtCore.QRect(1060, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.qInboxLabel = QtWidgets.QLabel(Form)
        self.qInboxLabel.setGeometry(QtCore.QRect(210, 90, 241, 81))
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
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.backButton.raise_()

        self.backButton.hide()

        self.firstLastLabel.setText(self.first + " " + self.last)

        self.questions = self.db.get('/PendingQuestions', None)
        self.q = []
        for x in self.questions:
            s = (self.getSubject(self.questions.get(x).get('subId')))
            if (self.subject == s):
                self.q.append(self.questions.get(x))

        self.showSomething()
        print(self.q)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Head Teacher\'s Home Page"))
        self.firstLastLabel.setText(_translate("Form", "display first and last name tgt"))
        self.logoutButton.setText(_translate("Form", "Log Out"))
        self.nextButton.setText(_translate("Form", "Next"))
        self.backButton.setText(_translate("Form", "Back"))

    def retranslateUi2(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        self.quesLabel.setText(self._translate("Form", "Question ID:"))
        self.courseIdLabel.setText(self._translate("Form", "Course ID:"))
        self.usernameLabel.setText(self._translate("Form", "Username Submitted:"))
        self.viewButton.setText(self._translate("Form", "View Question"))
        self.qInboxLabel.setText(self._translate("Form", "Question Inbox:"))

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
        print(str(self.start) + "start")
        print(str(self.stop) + "stop")
        print()
        self.length = len(self.q)

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

            self.selectQuestion = question(self.quesID, self.courseID, self.question, self.ansA,
                                           self.ansB, self.ansC, self.ansD, self.correctAns, self.level, self.username)

            font = QtGui.QFont()
            font.setPointSize(14)

            self.quesLabel = QtWidgets.QLabel(self.Form)
            self.quesLabel.setGeometry(QtCore.QRect(190, 210 + self.y, 161, 51))
            self.quesLabel.setFont(font)
            self.quesLabel.setObjectName("quesLabel")

            self.displayQuesId = QtWidgets.QLabel(self.Form)
            self.displayQuesId.setGeometry(QtCore.QRect(360, 210 + self.y, 131, 51))
            self.displayQuesId.setFont(font)
            self.displayQuesId.setObjectName("displayQuesId")

            self.courseIdLabel = QtWidgets.QLabel(self.Form)
            self.courseIdLabel.setGeometry(QtCore.QRect(510, 210 + self.y, 131, 51))
            self.courseIdLabel.setFont(font)
            self.courseIdLabel.setObjectName("courseIdLabel")

            self.displayCourseId = QtWidgets.QLabel(self.Form)
            self.displayCourseId.setGeometry(QtCore.QRect(660, 210 + self.y, 241, 51))
            self.displayCourseId.setFont(font)
            self.displayCourseId.setObjectName("displayCourseId")

            self.usernameLabel = QtWidgets.QLabel(self.Form)
            self.usernameLabel.setGeometry(QtCore.QRect(190, 260 + self.y, 251, 51))
            self.usernameLabel.setFont(font)
            self.usernameLabel.setObjectName("usernameLabel")

            self.displayUsername = QtWidgets.QLabel(self.Form)
            self.displayUsername.setGeometry(QtCore.QRect(460, 260 + self.y, 371, 51))
            self.displayUsername.setFont(font)
            self.displayUsername.setObjectName("displayTeachName")

            self.viewButton = QtWidgets.QPushButton(self.Form)
            self.viewButton.setGeometry(QtCore.QRect(940, 220 + self.y, 211, 81))
            self.viewButton.setFont(font)

            self.a.append(self.quesLabel)
            self.a.append(self.displayQuesId)
            self.a.append(self.displayCourseId)
            self.a.append(self.usernameLabel)
            self.a.append(self.viewButton)
            self.a.append(self.courseIdLabel)
            self.a.append(self.displayUsername)

            for x in self.a:
                x.show()

            self.viewButton.clicked.connect(lambda checked, arg=self.selectQuestion: self.viewQuestion(arg))

            self.quesLabel.raise_()
            self.displayQuesId.raise_()
            self.courseIdLabel.raise_()
            self.displayCourseId.raise_()
            self.usernameLabel.raise_()
            self.displayUsername.raise_()
            self.viewButton.raise_()
            self.nextButton.raise_()

            self.retranslateUi2(self.Form)

            self.displayQuesId.setText(self.quesID)
            self.displayCourseId.setText(self.courseID)
            self.displayUsername.setText(self.username)

            self.y += 150

            if self.start == 0:
                self.backButton.hide()

            if i == self.stop - len(self.q):
                break

            if i == len(self.q) - 1:
                self.nextButton.hide()
                break

    def getSubject(self, subId):
        subject = ""
        for i in range(len(subId)):
            if not (subId[i].isdigit()):
                subject += subId[i]
        return subject

    def viewQuestion(self, x):
        print(x.getQuestion())
        self.window = QtWidgets.QMainWindow()
        self.ui = questionDetailPage.Ui_Form()
        self.ui.setupUi(self.window, x, self.ht)
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
