# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buckshot.ui'
#
# Created: Mon Nov  9 16:46:38 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_buckshot(object):
    def setupUi(self, buckshot):
        buckshot.setObjectName("buckshot")
        buckshot.setEnabled(True)
        buckshot.resize(875, 748)
        self.numbersField = QtWidgets.QLineEdit(buckshot)
        self.numbersField.setGeometry(QtCore.QRect(220, 20, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.numbersField.setFont(font)
        self.numbersField.setText("")
        self.numbersField.setFrame(True)
        self.numbersField.setObjectName("numbersField")
        self.label = QtWidgets.QLabel(buckshot)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(buckshot)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 781, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.goButton = QtWidgets.QPushButton(buckshot)
        self.goButton.setGeometry(QtCore.QRect(230, 670, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.goButton.setFont(font)
        self.goButton.setObjectName("goButton")
        self.markerNameField = QtWidgets.QLineEdit(buckshot)
        self.markerNameField.setGeometry(QtCore.QRect(190, 620, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.markerNameField.setFont(font)
        self.markerNameField.setText("")
        self.markerNameField.setFrame(True)
        self.markerNameField.setObjectName("markerNameField")
        self.label_11 = QtWidgets.QLabel(buckshot)
        self.label_11.setGeometry(QtCore.QRect(10, 610, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.DdField = QtWidgets.QPlainTextEdit(buckshot)
        self.DdField.setEnabled(True)
        self.DdField.setGeometry(QtCore.QRect(360, 180, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DdField.setFont(font)
        self.DdField.setReadOnly(True)
        self.DdField.setPlainText("")
        self.DdField.setObjectName("DdField")
        self.DMmField = QtWidgets.QPlainTextEdit(buckshot)
        self.DMmField.setEnabled(True)
        self.DMmField.setGeometry(QtCore.QRect(360, 290, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DMmField.setFont(font)
        self.DMmField.setReadOnly(True)
        self.DMmField.setObjectName("DMmField")
        self.DMSsField = QtWidgets.QPlainTextEdit(buckshot)
        self.DMSsField.setEnabled(True)
        self.DMSsField.setGeometry(QtCore.QRect(360, 450, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DMSsField.setFont(font)
        self.DMSsField.setReadOnly(True)
        self.DMSsField.setObjectName("DMSsField")
        self.label_3 = QtWidgets.QLabel(buckshot)
        self.label_3.setGeometry(QtCore.QRect(190, 180, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(buckshot)
        self.label_4.setGeometry(QtCore.QRect(100, 290, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(buckshot)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.URLField = QtWidgets.QLineEdit(buckshot)
        self.URLField.setGeometry(QtCore.QRect(470, 620, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.URLField.setFont(font)
        self.URLField.setText("")
        self.URLField.setFrame(True)
        self.URLField.setObjectName("URLField")
        self.label_12 = QtWidgets.QLabel(buckshot)
        self.label_12.setGeometry(QtCore.QRect(400, 610, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(buckshot)
        self.label_13.setGeometry(QtCore.QRect(330, 130, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(buckshot)
        self.numbersField.textChanged['QString'].connect(buckshot.calcLatLon)
        self.goButton.clicked.connect(buckshot.createMarkers)
        QtCore.QMetaObject.connectSlotsByName(buckshot)

    def retranslateUi(self, buckshot):
        _translate = QtCore.QCoreApplication.translate
        buckshot.setWindowTitle(_translate("buckshot", "SARSoft Buckshot"))
        self.label.setText(_translate("buckshot", "Numbers"))
        self.label_2.setText(_translate("buckshot", "Only enter the numbers you received, in order.\n"
"Do not enter any spaces, punctuation, or minus sign."))
        self.goButton.setText(_translate("buckshot", "Create SARSoft Markers"))
        self.label_11.setText(_translate("buckshot", "Marker Name"))
        self.label_3.setText(_translate("buckshot", "Decimal Degrees\n"
"(Dd)"))
        self.label_4.setText(_translate("buckshot", "Degrees and Decimal Minutes\n"
"(DMm)"))
        self.label_5.setText(_translate("buckshot", "Degrees, Minutes, and Decimal Seconds\n"
"(DMSs)"))
        self.label_12.setText(_translate("buckshot", "URL"))
        self.label_13.setText(_translate("buckshot", "Possibilities"))
