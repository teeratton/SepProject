# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkQuestionStatus.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from firebase import firebase
from PyQt5 import QtCore, QtGui, QtWidgets
from question import question
from teacher import teacher
import teacherPage
import questionDetailPage
import uploadQuestionPage
import firstLoginPage

class Ui_Form(object):
    def setupUi(self, Form,t):
        Form.setObjectName("Form")
        self.t = t
        self.Form=Form
        
        self.first = self.t.getFirst()
        self.last = self.t.getLast()
        self.subject = self.t.getSubjects()
        self.username = self.t.getUsername()
        print("Current username is: " + self.username)

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
        #self.nextButton.clicked.connect(self.increment)
        self.backButton = QtWidgets.QPushButton(self.Form)
        self.backButton.setGeometry(QtCore.QRect(750, 650, 181, 71))
        #self.backButton.clicked.connect(self.decrement)

        self.logoutButton.clicked.connect(self.logOut)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.nextButton.raise_()
        self.nextButton.hide()
        self.backButton.raise_()
        self.backButton.hide()


        self.firstLastLabel.setText(self.first + " " + self.last)
        self.questions = self.db.get('/PendingQuestions', None)
        self.rejects = self.db.get('/RejectQuestions',None)

        self.q = []
        for x in self.questions:
            tu = (self.questions.get(x).get('teacherUsername'))
            if (self.username == tu):
                self.q.append(self.questions.get(x))

        self.re = []
        for x in self.rejects:
            tu = (self.rejects.get(x).get('teacherUsername'))
            if (self.username == tu):
                self.re.append(self.rejects.get(x))

        if (len(self.q) != 0) and (len(self.re) != 0):
            print("KAO WEII")
            self.showSomething()
        else:
            self.nextButton.hide()
            
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
        print("KAO JINGJING")
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

            self.a.append(self.quesLabel)
            self.a.append(self.displayQuesId)
            self.a.append(self.displayCourseId)
            self.a.append(self.courseIdLabel)

            for x in self.a:
                x.show()

            self.quesLabel.raise_()
            self.displayQuesId.raise_()
            self.courseIdLabel.raise_()
            self.displayCourseId.raise_()
            self.nextButton.raise_()

            self.retranslateUi2(self.Form)

            self.displayQuesId.setText(self.quesID)
            self.displayCourseId.setText(self.courseID)
  
            self.y += 150

            if self.start == 0:
                self.backButton.hide()

            if i == self.stop - len(self.q):
                break

            if i == len(self.q) - 1:
                self.nextButton.hide()
                break

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Check Exam Questions Status"))
        self.firstLastLabel.setText(_translate("Form", "display teacher full name"))
        self.logoutButton.setText(_translate("Form", "Log Out"))
        self.qInboxLabel.setText(_translate("Form", "Question Inbox:"))
        self.backButton.setText(_translate("Form", "Back"))

    def retranslateUi2(self,Form):
        self._translate = QtCore.QCoreApplication.translate
        self.quesLabel.setText(_translate("Form", "Question ID:"))
        self.courseLabel.setText(_translate("Form", "Course ID:"))
        '''
        self.statusLabel.setText(_translate("Form", "Status:"))
        self.displayStatus.setText(_translate("Form", "Not Approved"))
        self.editButton.setText(_translate("Form", "Edit "))
        self.commentLabel.setText(_translate("Form", "Comment:"))
        self.displayCommentBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I don\'t think the choice A is the correct answer since the theory of relativity conflicts with this answer. But i think this is a really interesting question. </span></p></body></html>"))
        self.deleteButton.setText(_translate("Form", "Delete"))
'''

    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = teacherPage.Ui_Form()
        self.ui.setupUi(self.window, self.t)
        self.Form.hide()
        self.window.show()

    def logOut(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = firstLoginPage.Ui_Login()
        self.ui.setupUi(self.window)
        self.Form.hide()
        self.window.show()

    def getSubject(self, subId):
        subject = ""
        for i in range(len(subId)):
            if not (subId[i].isdigit()):
                subject += subId[i]
        return subject



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

