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
    def setupUi(self, Form,ht):
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


        Form.resize(1262, 819)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, -20, 721, 161))
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
        self.logoutButton.setGeometry(QtCore.QRect(1060, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.qInboxLabel = QtWidgets.QLabel(Form)
        self.qInboxLabel.setGeometry(QtCore.QRect(110, 90, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.qInboxLabel.setFont(font)
        self.qInboxLabel.setObjectName("qInboxLabel")

        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(110, 170, 1041, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1039, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setMinimumSize(50,300)


        #self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy)
        #self.scrollAreasetVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.firstLastLabel.setText(self.first + " " + self.last)

        self.questions = self.db.get('/PendingQuestions',None)
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


    def retranslateUi2(self,Form):
        _translate = QtCore.QCoreApplication.translate
        self.quesLabel.setText(_translate("Form", "Question ID:"))
        self.courseIdLabel.setText(_translate("Form", "Course ID:"))
        self.usernameLabel.setText(_translate("Form", "Username Submitted:"))
        self.viewButton.setText(_translate("Form", "View Question"))
        self.qInboxLabel.setText(_translate("Form", "Question Inbox:"))


    def doSomething(self):
        pass


    def showSomething(self):

        for i in range (len(self.q)):
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

            self.selectQuestion = question(self.quesID,self.courseID,self.question,self.ansA,
                                           self.ansB,self.ansC,self.ansD,self.correctAns,self.level,self.username)



            font = QtGui.QFont()
            font.setPointSize(14)


            self.quesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.quesLabel.setGeometry(QtCore.QRect(40, 10 + self.y, 161, 51))
            self.quesLabel.setFont(font)
            self.quesLabel.setObjectName("quesLabel")

            self.displayQuesId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.displayQuesId.setGeometry(QtCore.QRect(210, 10 + self.y, 131, 51))
            self.displayQuesId.setFont(font)
            self.displayQuesId.setObjectName("displayQuesId")

            self.courseIdLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.courseIdLabel.setGeometry(QtCore.QRect(360, 10 + self.y, 131, 51))
            self.courseIdLabel.setFont(font)
            self.courseIdLabel.setObjectName("courseIdLabel")

            self.displayCourseId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.displayCourseId.setGeometry(QtCore.QRect(510, 10 + self.y, 241, 51))
            self.displayCourseId.setFont(font)
            self.displayCourseId.setObjectName("displayCourseId")

            self.usernameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.usernameLabel.setGeometry(QtCore.QRect(40, 60 + self.y, 251, 51))
            self.usernameLabel.setFont(font)
            self.usernameLabel.setObjectName("usernameLabel")

            self.displayUsername = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.displayUsername.setGeometry(QtCore.QRect(310, 60 + self.y, 371, 51))
            self.displayUsername.setFont(font)
            self.displayUsername.setObjectName("displayTeachName")

            self.viewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.viewButton.setGeometry(QtCore.QRect(790, 20 + self.y, 211, 81))
            self.viewButton.setFont(font)

            self.viewButton.clicked.connect(lambda checked, arg = self.selectQuestion : self.viewQuestion(arg) )

            self.quesLabel.raise_()
            self.displayQuesId.raise_()
            self.courseIdLabel.raise_()
            self.displayCourseId.raise_()
            self.usernameLabel.raise_()
            self.displayUsername.raise_()
            self.viewButton.raise_()

            self.retranslateUi2(self.Form)

            self.displayQuesId.setText(self.quesID)
            self.displayCourseId.setText(self.courseID)
            self.displayUsername.setText(self.username)

            self.scrollArea.update()
            self.scrollArea.setVisible(True)
            self.y += 100



    def getSubject(self,subId):
        subject =""
        for i in range(len(subId)):
            if not (subId[i].isdigit()):
                subject += subId[i]
        return subject

    def viewQuestion(self,x):
        print(x.getQuestion())
        self.window = QtWidgets.QMainWindow()
        self.ui = questionDetailPage.Ui_Form()
        self.ui.setupUi(self.window,x,self.ht)
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

