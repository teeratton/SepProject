# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'headTeacherPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1262, 824)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 0, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.firstLastLabel = QtWidgets.QLabel(Form)
        self.firstLastLabel.setGeometry(QtCore.QRect(410, 130, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.firstLastLabel.setFont(font)
        self.firstLastLabel.setObjectName("firstLastLabel")
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setGeometry(QtCore.QRect(1040, 40, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.qInboxLabel = QtWidgets.QLabel(Form)
        self.qInboxLabel.setGeometry(QtCore.QRect(40, 210, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.qInboxLabel.setFont(font)
        self.qInboxLabel.setObjectName("qInboxLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Head Teacher\'s Home Page"))
        self.firstLastLabel.setText(_translate("Form", "display first and last name tgt"))
        self.logoutButton.setText(_translate("Form", "Log Out"))
        self.qInboxLabel.setText(_translate("Form", "Question Inbox:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

