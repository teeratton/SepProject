from PyQt5 import QtCore, QtGui, QtWidgets
from teacher import teacher
import uploadSystem
import statusSystem
import loginSystem
import generateSystem


class Ui_Form(object):
    def setupUi(self, Form,t):
        self.t = t
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(1265, 825)
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(360, 10, 551, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.firstLastLabel = QtWidgets.QLabel(Form)
        self.firstLastLabel.setGeometry(QtCore.QRect(410, 150, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.firstLastLabel.setFont(font)
        self.firstLastLabel.setObjectName("firstLastLabel")
        self.uploadButton = QtWidgets.QPushButton(Form)
        self.uploadButton.setGeometry(QtCore.QRect(370, 290, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.uploadButton.setFont(font)
        self.uploadButton.setObjectName("uploadButton")
        self.checkButton = QtWidgets.QPushButton(Form)
        self.checkButton.setGeometry(QtCore.QRect(370, 440, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName("checkButton")
        self.generateButton = QtWidgets.QPushButton(Form)
        self.generateButton.setGeometry(QtCore.QRect(370, 590, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setGeometry(QtCore.QRect(1030, 710, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.checkButton.clicked.connect(self.check)
        self.uploadButton.clicked.connect(self.upload)
        self.generateButton.clicked.connect(self.generate)
        self.logoutButton.clicked.connect(self.logOut)

        self.firstLastLabel.setText(self.t.getFirst() + " " + self.t.getLast())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Teacher\'s Home Page"))
        self.firstLastLabel.setText(_translate("Form", "display first and last name tgt"))
        self.uploadButton.setText(_translate("Form", "Upload An Exam Question"))
        self.checkButton.setText(_translate("Form", "Check Exam Questions Status"))
        self.generateButton.setText(_translate("Form", "Generate An Exam"))
        self.logoutButton.setText(_translate("Form", "Log Out"))

    def upload(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uploadSystem.uploadSystem()
        self.ui.setupUi(self.window,self.t)
        self.Form.hide()
        self.window.show()

    def generate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = generateSystem.generateSystem()
        self.ui.setupUi(self.window, self.t)
        self.Form.hide()
        self.window.show()


    def logOut(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = loginSystem.loginSystem()
        self.ui.setupUi(self.window)
        self.Form.hide()
        self.window.show()

    def check(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = statusSystem.statusSystem()
        self.ui.setupUi(self.window,self.t)
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

