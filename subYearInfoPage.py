# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subYearInfoPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubYear(object):
    def setupUi(self, Form,first,last,username,role):
        self.subjects = []
        self.first = first
        self.last = last
        self.username = username
        self.role = role
        Form.setObjectName("Form")
        Form.resize(1269, 825)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 20, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sciCheck = QtWidgets.QCheckBox(Form)
        self.sciCheck.setGeometry(QtCore.QRect(820, 350, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sciCheck.setFont(font)
        self.sciCheck.setObjectName("sciCheck")
        self.mathCheck = QtWidgets.QCheckBox(Form)
        self.mathCheck.setGeometry(QtCore.QRect(400, 550, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mathCheck.setFont(font)
        self.mathCheck.setObjectName("mathCheck")
        self.hisCheck = QtWidgets.QCheckBox(Form)
        self.hisCheck.setGeometry(QtCore.QRect(400, 450, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hisCheck.setFont(font)
        self.hisCheck.setObjectName("hisCheck")
        self.musicCheck = QtWidgets.QCheckBox(Form)
        self.musicCheck.setGeometry(QtCore.QRect(400, 650, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.musicCheck.setFont(font)
        self.musicCheck.setObjectName("musicCheck")
        self.artCheck = QtWidgets.QCheckBox(Form)
        self.artCheck.setGeometry(QtCore.QRect(20, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.artCheck.setFont(font)
        self.artCheck.setObjectName("artCheck")
        self.thaiCheck = QtWidgets.QCheckBox(Form)
        self.thaiCheck.setGeometry(QtCore.QRect(820, 550, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thaiCheck.setFont(font)
        self.thaiCheck.setObjectName("thaiCheck")
        self.engCheck = QtWidgets.QCheckBox(Form)
        self.engCheck.setGeometry(QtCore.QRect(400, 250, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.engCheck.setFont(font)
        self.engCheck.setObjectName("engCheck")
        self.peCheck = QtWidgets.QCheckBox(Form)
        self.peCheck.setGeometry(QtCore.QRect(820, 150, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.peCheck.setFont(font)
        self.peCheck.setObjectName("peCheck")
        self.religionCheck = QtWidgets.QCheckBox(Form)
        self.religionCheck.setGeometry(QtCore.QRect(820, 650, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.religionCheck.setFont(font)
        self.religionCheck.setObjectName("religionCheck")
        self.socialCheck = QtWidgets.QCheckBox(Form)
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
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(610, 460, 181, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
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
        if(self.mathCheck.isChecked()):
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("math"+x)
            print(self.subjects)
        elif (self.sciCheck.isChecked()):
            print("sci")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("sci" + x)
            print(self.subjects)
        elif (self.hisCheck.isChecked()):
            print("his")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("his" + x)
            print(self.subjects)
        elif (self.musicCheck.isChecked()):
            print("music")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("music" + x)
            print(self.subjects)
        elif (self.artCheck.isChecked()):
            print("art")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("art" + x)
            print(self.subjects)
        elif (self.thaiCheck.isChecked()):
            print("thai")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("thai" + x)
            print(self.subjects)
        elif (self.engCheck.isChecked()):
            print("eng")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("eng" + x)
            print(self.subjects)
        elif (self.peCheck.isChecked()):
            print("pe")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("pe" + x)
            print(self.subjects)
        elif (self.religionCheck.isChecked()):
            print("religion")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("religion" + x)
            print(self.subjects)
        elif (self.socialCheck.isChecked()):
            print("social")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("social" + x)
            print(self.subjects)
        elif (self.compCheck.isChecked()):
            print("comp")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("comp" + x)
            print(self.subjects)
        elif (self.geoCheck.isChecked()):
            print("geo")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("geo" + x)
            print(self.subjects)
        elif (self.bioCheck.isChecked()):
            print("bio")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("bio" + x)
            print(self.subjects)
        elif (self.chemCheck.isChecked()):
            print("chem")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("chem" + x)
            print(self.subjects)
        elif (self.physicCheck.isChecked()):
            print("physic")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("physic" + x)
            print(self.subjects)
        elif (self.dramaCheck.isChecked()):
            print("drama")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("drama" + x)
            print(self.subjects)
        elif (self.bandCheck.isChecked()):
            print("band")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("band" + x)
            print(self.subjects)
        elif (self.chiorCheck.isChecked()):
            print("choir")
            years = self.mathEntry.text()
            for x in years.split(','):
                self.subjects.append("chior" + x)
            print(self.subjects)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_SubYear()
    #ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

