# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buckshot.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_buckshot(object):
    def setupUi(self, buckshot):
        buckshot.setObjectName("buckshot")
        buckshot.setEnabled(True)
        buckshot.resize(883, 762)
        self.coordsField = QtWidgets.QLineEdit(buckshot)
        self.coordsField.setGeometry(QtCore.QRect(270, 20, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.coordsField.setFont(font)
        self.coordsField.setText("")
        self.coordsField.setFrame(True)
        self.coordsField.setObjectName("coordsField")
        self.label = QtWidgets.QLabel(buckshot)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(buckshot)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 871, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.goButton = QtWidgets.QPushButton(buckshot)
        self.goButton.setGeometry(QtCore.QRect(40, 680, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.goButton.setFont(font)
        self.goButton.setObjectName("goButton")
        self.markerNameField = QtWidgets.QLineEdit(buckshot)
        self.markerNameField.setGeometry(QtCore.QRect(160, 630, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.markerNameField.setFont(font)
        self.markerNameField.setText("")
        self.markerNameField.setFrame(True)
        self.markerNameField.setObjectName("markerNameField")
        self.label_11 = QtWidgets.QLabel(buckshot)
        self.label_11.setGeometry(QtCore.QRect(-10, 620, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(buckshot)
        self.label_3.setGeometry(QtCore.QRect(190, 170, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(buckshot)
        self.label_4.setGeometry(QtCore.QRect(100, 280, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(buckshot)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.URLField = QtWidgets.QLineEdit(buckshot)
        self.URLField.setGeometry(QtCore.QRect(420, 700, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.URLField.setFont(font)
        self.URLField.setText("")
        self.URLField.setFrame(True)
        self.URLField.setObjectName("URLField")
        self.label_12 = QtWidgets.QLabel(buckshot)
        self.label_12.setGeometry(QtCore.QRect(350, 690, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(buckshot)
        self.label_13.setGeometry(QtCore.QRect(0, 120, 871, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(buckshot)
        self.label_6.setGeometry(QtCore.QRect(370, 730, 501, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gpxFileNameField = QtWidgets.QLineEdit(buckshot)
        self.gpxFileNameField.setGeometry(QtCore.QRect(420, 630, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.gpxFileNameField.setFont(font)
        self.gpxFileNameField.setText("")
        self.gpxFileNameField.setFrame(True)
        self.gpxFileNameField.setObjectName("gpxFileNameField")
        self.label_14 = QtWidgets.QLabel(buckshot)
        self.label_14.setGeometry(QtCore.QRect(350, 620, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(buckshot)
        self.label_7.setGeometry(QtCore.QRect(370, 660, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gpxBrowseButton = QtWidgets.QPushButton(buckshot)
        self.gpxBrowseButton.setGeometry(QtCore.QRect(790, 630, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gpxBrowseButton.setFont(font)
        self.gpxBrowseButton.setObjectName("gpxBrowseButton")
        self.label_8 = QtWidgets.QLabel(buckshot)
        self.label_8.setGeometry(QtCore.QRect(20, 590, 831, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.DdField = QtWidgets.QListWidget(buckshot)
        self.DdField.setGeometry(QtCore.QRect(360, 170, 451, 101))
        self.DdField.setObjectName("DdField")
        self.DMmField = QtWidgets.QListWidget(buckshot)
        self.DMmField.setGeometry(QtCore.QRect(360, 280, 451, 131))
        self.DMmField.setObjectName("DMmField")
        self.DMSsField = QtWidgets.QListWidget(buckshot)
        self.DMSsField.setGeometry(QtCore.QRect(360, 420, 451, 171))
        self.DMSsField.setObjectName("DMSsField")

        self.retranslateUi(buckshot)
        self.coordsField.textChanged['QString'].connect(buckshot.calcLatLon)
        self.goButton.clicked.connect(buckshot.createMarkers)
        self.gpxBrowseButton.clicked['bool'].connect(buckshot.gpxSetFileName)
        self.markerNameField.textChanged['QString'].connect(buckshot.markerNameChanged)
        self.DdField.itemClicked['QListWidgetItem*'].connect(buckshot.possibilityDdClicked)
        self.DMmField.itemClicked['QListWidgetItem*'].connect(buckshot.possibilityDMmClicked)
        self.DMSsField.itemClicked['QListWidgetItem*'].connect(buckshot.possibilityDMSsClicked)
        QtCore.QMetaObject.connectSlotsByName(buckshot)
        buckshot.setTabOrder(self.coordsField, self.markerNameField)
        buckshot.setTabOrder(self.markerNameField, self.gpxFileNameField)
        buckshot.setTabOrder(self.gpxFileNameField, self.URLField)
        buckshot.setTabOrder(self.URLField, self.goButton)
        buckshot.setTabOrder(self.goButton, self.gpxBrowseButton)

    def retranslateUi(self, buckshot):
        _translate = QtCore.QCoreApplication.translate
        buckshot.setWindowTitle(_translate("buckshot", "SARSoft Buckshot"))
        self.label.setText(_translate("buckshot", "Coordinates"))
        self.label_2.setText(_translate("buckshot", "Enter only the numbers from the raw coordinates that you were given.\n"
"Do not use spaces or any punctuation."))
        self.goButton.setText(_translate("buckshot", "Create Markers"))
        self.label_11.setText(_translate("buckshot", "Marker Name"))
        self.label_3.setText(_translate("buckshot", "Decimal Degrees\n"
"(Dd)"))
        self.label_4.setText(_translate("buckshot", "Degrees and Decimal Minutes\n"
"(DMm)"))
        self.label_5.setText(_translate("buckshot", "Degrees, Minutes, and Decimal Seconds\n"
"(DMSs)"))
        self.label_12.setText(_translate("buckshot", "URL"))
        self.label_13.setText(_translate("buckshot", "Possibilities"))
        self.label_6.setText(_translate("buckshot", "Optional.  URL of a saved SARSoft map, hosted locally or on current network."))
        self.label_14.setText(_translate("buckshot", "GPX"))
        self.label_7.setText(_translate("buckshot", "Optional.  Full .gpx filename.  File is not written until \'Create Markers\' is clicked."))
        self.gpxBrowseButton.setText(_translate("buckshot", "Browse"))
        self.label_8.setText(_translate("buckshot", "Optional: Click the one possibility that most closely matches the report.  Click it again to clear."))

