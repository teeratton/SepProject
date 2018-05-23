# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warningDupNamePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 513)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 10, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 200, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.uNameGeneratedLabel = QtWidgets.QLabel(Form)
        self.uNameGeneratedLabel.setGeometry(QtCore.QRect(140, 260, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.uNameGeneratedLabel.setFont(font)
        self.uNameGeneratedLabel.setObjectName("uNameGeneratedLabel")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(50, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.confirmButton = QtWidgets.QPushButton(Form)
        self.confirmButton.setGeometry(QtCore.QRect(350, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 360, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Warning"))
        self.label_2.setText(_translate("Form", "This username already exists in the system."))
        self.label_3.setText(_translate("Form", "Here is a possible username:"))
        self.uNameGeneratedLabel.setText(_translate("Form", "_______________________"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.confirmButton.setText(_translate("Form", "Confirm"))
        self.label_4.setText(_translate("Form", "Do you want to use this username instead?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

