# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regisNewAccountPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1271, 823)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 1051, 191))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fNameEntry = QtWidgets.QLineEdit(Form)
        self.fNameEntry.setGeometry(QtCore.QRect(520, 260, 501, 61))
        self.fNameEntry.setObjectName("fNameEntry")
        self.fNameLabel = QtWidgets.QLabel(Form)
        self.fNameLabel.setGeometry(QtCore.QRect(240, 250, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fNameLabel.setFont(font)
        self.fNameLabel.setObjectName("fNameLabel")
        self.lNameLabel = QtWidgets.QLabel(Form)
        self.lNameLabel.setGeometry(QtCore.QRect(240, 360, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lNameLabel.setFont(font)
        self.lNameLabel.setObjectName("lNameLabel")
        self.lNameEntry = QtWidgets.QLineEdit(Form)
        self.lNameEntry.setGeometry(QtCore.QRect(520, 370, 501, 61))
        self.lNameEntry.setObjectName("lNameEntry")
        self.uNameLabel = QtWidgets.QLabel(Form)
        self.uNameLabel.setGeometry(QtCore.QRect(240, 470, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.uNameLabel.setFont(font)
        self.uNameLabel.setObjectName("uNameLabel")
        self.uNameEntry = QtWidgets.QLineEdit(Form)
        self.uNameEntry.setGeometry(QtCore.QRect(520, 480, 501, 61))
        self.uNameEntry.setObjectName("uNameEntry")
        self.roleLabel = QtWidgets.QLabel(Form)
        self.roleLabel.setGeometry(QtCore.QRect(240, 580, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.roleLabel.setFont(font)
        self.roleLabel.setObjectName("roleLabel")
        self.roleEntry = QtWidgets.QComboBox(Form)
        self.roleEntry.setGeometry(QtCore.QRect(520, 590, 231, 61))
        self.roleEntry.setObjectName("roleEntry")
        self.roleEntry.addItem("")
        self.roleEntry.addItem("")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(1030, 710, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Register A New Account"))
        self.fNameLabel.setText(_translate("Form", "First Name: "))
        self.lNameLabel.setText(_translate("Form", "Last Name: "))
        self.uNameLabel.setText(_translate("Form", "Username:"))
        self.roleLabel.setText(_translate("Form", "Role:"))
        self.roleEntry.setItemText(0, _translate("Form", "Teacher"))
        self.roleEntry.setItemText(1, _translate("Form", "Head Teacher"))
        self.nextButton.setText(_translate("Form", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

