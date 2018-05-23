# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subYearInfoPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random
import string
from firebase import firebase

class Ui_SubYear(object):
    def setupUi(self, Form,first,last,username,role):
        self.db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')
        self.subjects = {}
        self.first = first
        self.last = last
        self.username = username
        self.role = role
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(1269, 825)
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(270, 20, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sciCheck = QtWidgets.QCheckBox(self.Form)
        self.sciCheck.setGeometry(QtCore.QRect(820, 350, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sciCheck.setFont(font)
        self.sciCheck.setObjectName("sciCheck")
        self.mathCheck = QtWidgets.QCheckBox(self.Form)
        self.mathCheck.setGeometry(QtCore.QRect(400, 550, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mathCheck.setFont(font)
        self.mathCheck.setObjectName("mathCheck")
        self.hisCheck = QtWidgets.QCheckBox(self.Form)
        self.hisCheck.setGeometry(QtCore.QRect(400, 450, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hisCheck.setFont(font)
        self.hisCheck.setObjectName("hisCheck")
        self.musicCheck = QtWidgets.QCheckBox(self.Form)
        self.musicCheck.setGeometry(QtCore.QRect(400, 650, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.musicCheck.setFont(font)
        self.musicCheck.setObjectName("musicCheck")
        self.artCheck = QtWidgets.QCheckBox(self.Form)
        self.artCheck.setGeometry(QtCore.QRect(20, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.artCheck.setFont(font)
        self.artCheck.setObjectName("artCheck")
        self.thaiCheck = QtWidgets.QCheckBox(self.Form)
        self.thaiCheck.setGeometry(QtCore.QRect(820, 550, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thaiCheck.setFont(font)
        self.thaiCheck.setObjectName("thaiCheck")
        self.engCheck = QtWidgets.QCheckBox(self.Form)
        self.engCheck.setGeometry(QtCore.QRect(400, 250, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.engCheck.setFont(font)
        self.engCheck.setObjectName("engCheck")
        self.peCheck = QtWidgets.QCheckBox(self.Form)
        self.peCheck.setGeometry(QtCore.QRect(820, 150, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.peCheck.setFont(font)
        self.peCheck.setObjectName("peCheck")
        self.religionCheck = QtWidgets.QCheckBox(self.Form)
        self.religionCheck.setGeometry(QtCore.QRect(820, 650, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.religionCheck.setFont(font)
        self.religionCheck.setObjectName("religionCheck")
        self.socialCheck = QtWidgets.QCheckBox(self.Form)
        self.socialCheck.setGeometry(QtCore.QRect(820, 450, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.socialCheck.setFont(font)
        self.socialCheck.setObjectName("socialCheck")
        self.compCheck = QtWidgets.QCheckBox(Form)
        self.compCheck.setGeometry(QtCore.QRect(20, 650, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.compCheck.setFont(font)
        self.compCheck.setObjectName("compCheck")
        self.geoCheck = QtWidgets.QCheckBox(Form)
        self.geoCheck.setGeometry(QtCore.QRect(400, 350, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.geoCheck.setFont(font)
        self.geoCheck.setObjectName("geoCheck")
        self.bioCheck = QtWidgets.QCheckBox(Form)
        self.bioCheck.setGeometry(QtCore.QRect(20, 350, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bioCheck.setFont(font)
        self.bioCheck.setObjectName("bioCheck")
        self.chemCheck = QtWidgets.QCheckBox(Form)
        self.chemCheck.setGeometry(QtCore.QRect(20, 450, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chemCheck.setFont(font)
        self.chemCheck.setObjectName("chemCheck")
        self.physicCheck = QtWidgets.QCheckBox(Form)
        self.physicCheck.setGeometry(QtCore.QRect(820, 250, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.physicCheck.setFont(font)
        self.physicCheck.setObjectName("physicCheck")
        self.dramaCheck = QtWidgets.QCheckBox(Form)
        self.dramaCheck.setGeometry(QtCore.QRect(400, 150, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dramaCheck.setFont(font)
        self.dramaCheck.setObjectName("dramaCheck")
        self.bandCheck = QtWidgets.QCheckBox(Form)
        self.bandCheck.setGeometry(QtCore.QRect(20, 250, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bandCheck.setFont(font)
        self.bandCheck.setObjectName("bandCheck")
        self.chiorCheck = QtWidgets.QCheckBox(Form)
        self.chiorCheck.setGeometry(QtCore.QRect(20, 550, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chiorCheck.setFont(font)
        self.chiorCheck.setObjectName("chiorCheck")
        self.artEntry = QtWidgets.QLineEdit(Form)
        self.artEntry.setGeometry(QtCore.QRect(190, 160, 181, 41))
        self.artEntry.setObjectName("artEntry")
        self.bandEntry = QtWidgets.QLineEdit(Form)
        self.bandEntry.setGeometry(QtCore.QRect(190, 260, 181, 41))
        self.bandEntry.setObjectName("bandEntry")
        self.bioEntry = QtWidgets.QLineEdit(Form)
        self.bioEntry.setGeometry(QtCore.QRect(190, 360, 181, 41))
        self.bioEntry.setObjectName("bioEntry")
        self.chemEntry = QtWidgets.QLineEdit(Form)
        self.chemEntry.setGeometry(QtCore.QRect(190, 460, 181, 41))
        self.chemEntry.setObjectName("chemEntry")
        self.choirEntry = QtWidgets.QLineEdit(Form)
        self.choirEntry.setGeometry(QtCore.QRect(190, 560, 181, 41))
        self.choirEntry.setObjectName("choirEntry")
        self.compEntry = QtWidgets.QLineEdit(Form)
        self.compEntry.setGeometry(QtCore.QRect(190, 660, 181, 41))
        self.compEntry.setObjectName("compEntry")
        self.dramaEntry = QtWidgets.QLineEdit(Form)
        self.dramaEntry.setGeometry(QtCore.QRect(610, 160, 181, 41))
        self.dramaEntry.setObjectName("dramaEntry")
        self.engEntry = QtWidgets.QLineEdit(Form)
        self.engEntry.setGeometry(QtCore.QRect(610, 260, 181, 41))
        self.engEntry.setObjectName("engEntry")
        self.geoEntry = QtWidgets.QLineEdit(Form)
        self.geoEntry.setGeometry(QtCore.QRect(610, 360, 181, 41))
        self.geoEntry.setObjectName("geoEntry")
        self.hisEntry = QtWidgets.QLineEdit(Form)
        self.hisEntry.setGeometry(QtCore.QRect(610, 460, 181, 41))
        self.hisEntry.setObjectName("hisEntry")
        self.mathEntry = QtWidgets.QLineEdit(Form)
        self.mathEntry.setGeometry(QtCore.QRect(610, 560, 181, 41))
        self.mathEntry.setObjectName("mathEntry")
        self.musicEntry = QtWidgets.QLineEdit(Form)
        self.musicEntry.setGeometry(QtCore.QRect(610, 660, 181, 41))
        self.musicEntry.setObjectName("musicEntry")
        self.religionEntry = QtWidgets.QLineEdit(Form)
        self.religionEntry.setGeometry(QtCore.QRect(1060, 660, 181, 41))
        self.religionEntry.setObjectName("religionEntry")
        self.thaiEntry = QtWidgets.QLineEdit(Form)
        self.thaiEntry.setGeometry(QtCore.QRect(1060, 560, 181, 41))
        self.thaiEntry.setObjectName("thaiEntry")
        self.socialEntry = QtWidgets.QLineEdit(Form)
        self.socialEntry.setGeometry(QtCore.QRect(1060, 460, 181, 41))
        self.socialEntry.setObjectName("socialEntry")
        self.sciEntry = QtWidgets.QLineEdit(Form)
        self.sciEntry.setGeometry(QtCore.QRect(1060, 360, 181, 41))
        self.sciEntry.setObjectName("sciEntry")
        self.physicEntry = QtWidgets.QLineEdit(Form)
        self.physicEntry.setGeometry(QtCore.QRect(1060, 260, 181, 41))
        self.physicEntry.setObjectName("physicEntry")
        self.peEntry = QtWidgets.QLineEdit(Form)
        self.peEntry.setGeometry(QtCore.QRect(1060, 160, 181, 41))
        self.peEntry.setObjectName("peEntry")
        self.doneButton = QtWidgets.QPushButton(Form)
        self.doneButton.setGeometry(QtCore.QRect(1100, 740, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneButton.setFont(font)
        self.doneButton.setObjectName("doneButton")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Subject and Year Information"))
        self.sciCheck.setText(_translate("Form", "Science"))
        self.mathCheck.setText(_translate("Form", "Mathematics"))
        self.hisCheck.setText(_translate("Form", "History"))
        self.musicCheck.setText(_translate("Form", "Music"))
        self.artCheck.setText(_translate("Form", "Art"))
        self.thaiCheck.setText(_translate("Form", "Thai"))
        self.engCheck.setText(_translate("Form", "English"))
        self.peCheck.setText(_translate("Form", "P.E."))
        self.religionCheck.setText(_translate("Form", "Religion Studies"))
        self.socialCheck.setText(_translate("Form", "Social Studies"))
        self.compCheck.setText(_translate("Form", "Computer "))
        self.geoCheck.setText(_translate("Form", "Geography"))
        self.bioCheck.setText(_translate("Form", "Biology"))
        self.chemCheck.setText(_translate("Form", "Chemistry"))
        self.physicCheck.setText(_translate("Form", "Physics"))
        self.dramaCheck.setText(_translate("Form", "Drama"))
        self.bandCheck.setText(_translate("Form", "Band"))
        self.chiorCheck.setText(_translate("Form", "Choir"))
        self.doneButton.setText(_translate("Form", "Done"))
        self.doneButton.clicked.connect(self.done)
    
    def done(self):
        count = 1
        if(self.mathCheck.isChecked()):
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub"+str(count):"Mathematic"+x})
                count+=1


        if (self.sciCheck.isChecked()):
            years = self.sciEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub"+str(count):"Science"+x})
                count+=1

        if (self.hisCheck.isChecked()):
            years = self.hisEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub"+str(count):"History"+x})
                count+=1


        if (self.musicCheck.isChecked()):
            years = self.musicEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Music" + x})
                count += 1

        if (self.artCheck.isChecked()):
            years = self.artEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Art" + x})
                count += 1

        if (self.thaiCheck.isChecked()):
            years = self.thaiEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Thai" + x})
                count += 1

        if (self.engCheck.isChecked()):
            years = self.engEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "English" + x})
                count += 1

        if (self.peCheck.isChecked()):
            years = self.peEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "PE" + x})
                count += 1

        if (self.religionCheck.isChecked()):
            years = self.religionEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Religion" + x})
                count += 1

        if (self.socialCheck.isChecked()):
            years = self.socialEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Social Studies" + x})
                count += 1

        if (self.compCheck.isChecked()):
            years = self.compEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Computer" + x})
                count += 1

        if (self.geoCheck.isChecked()):
            years = self.geoEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Geography" + x})
                count += 1

        if (self.bioCheck.isChecked()):
            years = self.bioEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Biography" + x})
                count += 1

        if (self.chemCheck.isChecked()):
            years = self.chemEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Chemistry" + x})
                count += 1

        if (self.physicCheck.isChecked()):
            years = self.physicEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Physic" + x})
                count += 1

        if (self.dramaCheck.isChecked()):
            years = self.dramaEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Drama" + x})
                count += 1

        if (self.bandCheck.isChecked()):
            years = self.bandEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Band" + x})
                count += 1

        if (self.chiorCheck.isChecked()):
            years = self.choirEntry.text()
            for x in years.split(','):
                self.subjects.update({"sub" + str(count): "Choir" + x})
                count += 1
        else:
            print("please enter subject")

        self.password = self.generatePassword()
        print(self.subjects)
        print(self.password)

        self.teacher = {'first': self.first, 'last': self.last, 'password': self.password, 'role': self.role,
                    'subjects': self.subjects}

        self.dialog = QDialog(self.Form)
        layout = QVBoxLayout()

        subjectList = ""
        for i in self.subjects:
            subjectList += self.subjects.get(i) + ", "
        lusername = QLabel(self.Form)
        lusername.setText("Username : " + self.username + "\n" + "Password : " + self.password + "\n" + "First name: " + self.first +
                          "\n" + "Last name: " + self.last + "\n" + "Role: " + self.role + "\n" + "Subject: " + subjectList )
        layout.addWidget(lusername)

        confirm_button = QPushButton('Confirm')
        confirm_button.clicked.connect(self.Confirm)
        layout.addWidget(confirm_button)
        self.dialog.setLayout(layout)

        close_button = QPushButton('No')
        close_button.clicked.connect(self.dialog.close)
        layout.addWidget(close_button)
        self.dialog.setLayout(layout)

        self.dialog.show()


    def Confirm(self):
        self.db.put('Teachers',self.username,self.teacher)
        self.dialog.close()



    def generatePassword(self):
        passWord = ""
        for i in range(8):
            passWord += random.choice(string.ascii_letters + string.digits)
        return passWord


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_SubYear()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

