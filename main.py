# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import numpy as np
import joblib


class Ui_EmployeeRetention(object):
    def setupUi(self, EmployeeRetention):
        EmployeeRetention.setObjectName("EmployeeRetention")
        EmployeeRetention.resize(500, 300)
        EmployeeRetention.setStyleSheet("background-color: rgb(243, 235, 255);")
        EmployeeRetention.setAnimated(True)
        EmployeeRetention.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(EmployeeRetention)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 551, 651))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(243, 235, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.msg = QtWidgets.QMessageBox()
        self.label_31 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setTextFormat(QtCore.Qt.AutoText)
        self.label_31.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_31.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_31.setObjectName("label_31")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_31)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.el1 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el1.setFont(font)
        self.el1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el1.setObjectName("el1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.el1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_25 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.label_26 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.label_30 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.el2 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el2.setFont(font)
        self.el2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el2.setEditable(False)
        self.el2.setCurrentText("")
        self.el2.setMinimumContentsLength(2)
        self.el2.setObjectName("el2")
        self.el2.addItem("Non Travel")
        self.el2.addItem("Travel frequently")
        self.el2.addItem("Travel rarely")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.el2)
        self.el3 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el3.setFont(font)
        self.el3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el3.setObjectName("el3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.el3)
        self.el4 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el4.setFont(font)
        self.el4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el4.setObjectName("el4")
        self.el4.addItem("Human Resources")
        self.el4.addItem("Research & Development")
        self.el4.addItem("Sales")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.el4)
        self.el5 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el5.setFont(font)
        self.el5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el5.setObjectName("el5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.el5)
        self.el6 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el6.setFont(font)
        self.el6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el6.setObjectName("el6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.el6)
        self.el7 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el7.setFont(font)
        self.el7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el7.setObjectName("el7")
        self.el7.addItem("Human Resources")
        self.el7.addItem("Life Sciences")
        self.el7.addItem("Marketing")
        self.el7.addItem("Medical")
        self.el7.addItem("Other")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.el7)
        self.el8 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el8.setFont(font)
        self.el8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el8.setObjectName("el8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.el8)
        self.el9 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el9.setFont(font)
        self.el9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el9.setCurrentText("")
        self.el9.setObjectName("el9")
        self.el9.addItem("Female")
        self.el9.addItem("Male")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.el9)
        self.el10 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el10.setFont(font)
        self.el10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el10.setObjectName("el10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.el10)
        self.el11 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el11.setFont(font)
        self.el11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el11.setObjectName("el11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.el11)
        self.el12 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el12.setFont(font)
        self.el12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el12.setObjectName("el12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.el12)
        self.el13 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el13.setFont(font)
        self.el13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el13.setObjectName("el13")
        self.el13.addItem("Health Care Representation")
        self.el13.addItem("Laboratory Technician")
        self.el13.addItem("Manager")
        self.el13.addItem("Manufacturing Director")
        self.el13.addItem("Research Director")
        self.el13.addItem("Research Scientist")
        self.el13.addItem("Sales Executive")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.el13)
        self.el14 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el14.setFont(font)
        self.el14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el14.setObjectName("el14")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.el14)
        self.el15 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el15.setFont(font)
        self.el15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el15.setObjectName("el15")
        self.el15.addItem("Single")
        self.el15.addItem("Divorced")
        self.el15.addItem("Married")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.el15)
        self.el16 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el16.setFont(font)
        self.el16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el16.setObjectName("el16")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.el16)
        self.el17 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el17.setFont(font)
        self.el17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el17.setObjectName("el17")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.el17)
        self.el18 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el18.setFont(font)
        self.el18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el18.setObjectName("el18")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.el18)
        self.el19 = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el19.setFont(font)
        self.el19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el19.setObjectName("el19")
        self.el19.addItem("Yes")
        self.el19.addItem("No")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.el19)
        self.el20 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el20.setFont(font)
        self.el20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el20.setObjectName("el20")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.el20)
        self.el21 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el21.setFont(font)
        self.el21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el21.setObjectName("el21")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.el21)
        self.el22 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el22.setFont(font)
        self.el22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el22.setObjectName("el22")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.el22)
        self.el23 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el23.setFont(font)
        self.el23.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el23.setObjectName("el23")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.el23)
        self.el24 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el24.setFont(font)
        self.el24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el24.setObjectName("el24")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.FieldRole, self.el24)
        self.el25 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el25.setFont(font)
        self.el25.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el25.setObjectName("el25")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.el25)
        self.el26 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el26.setFont(font)
        self.el26.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el26.setObjectName("el26")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.FieldRole, self.el26)
        self.el27 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el27.setFont(font)
        self.el27.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el27.setObjectName("el27")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.FieldRole, self.el27)
        self.el28 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el28.setFont(font)
        self.el28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el28.setObjectName("el28")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.FieldRole, self.el28)
        self.el29 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.el29.setFont(font)
        self.el29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.el29.setObjectName("el29")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.FieldRole, self.el29)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(750, 0, 361, 901))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(170, 142, 244);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.listbox1 = QtWidgets.QListWidget(self.frame_2)
        self.listbox1.setGeometry(QtCore.QRect(10, 250, 301, 431))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        self.listbox1.setFont(font)
        self.listbox1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listbox1.setObjectName("listbox1")
        self.listbox1.clicked.connect(self.update)
        self.csv_open = QtWidgets.QPushButton(self.frame_2)
        self.csv_open.setGeometry(QtCore.QRect(90, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.csv_open.setFont(font)
        self.csv_open.setStyleSheet("background-color: rgb(250, 154, 155);")
        self.csv_open.setObjectName("csv_open")
        self.csv_open.clicked.connect(self.open_csv)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(100, 130, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(90, 650, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color: rgb(247, 191, 194);")
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.get_entry_data)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(190, 650, 61, 20))
        self.save.setFont(font)
        self.save.setStyleSheet("background-color: rgb(247, 191, 194);")
        self.save.clicked.connect(self.save_entry_data)
        EmployeeRetention.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeRetention)
        self.el2.setCurrentIndex(-1)
        self.el4.setCurrentIndex(-1)
        self.el7.setCurrentIndex(-1)
        self.el9.setCurrentIndex(-1)
        self.el13.setCurrentIndex(-1)
        self.el15.setCurrentIndex(-1)
        self.el19.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(EmployeeRetention)

    def retranslateUi(self, EmployeeRetention):
        _translate = QtCore.QCoreApplication.translate
        EmployeeRetention.setWindowTitle(_translate("EmployeeRetention", "MainWindow"))
        self.label_31.setText(_translate("EmployeeRetention", "Please enter the employee details"))
        self.label_2.setText(_translate("EmployeeRetention", "Enter Age:"))
        self.label_3.setText(_translate("EmployeeRetention", "Business Travel:"))
        self.label_4.setText(_translate("EmployeeRetention", "Enter Daily rate:"))
        self.label_5.setText(_translate("EmployeeRetention", "Enter Department:"))
        self.label_6.setText(_translate("EmployeeRetention", "Enter distance from home:"))
        self.label_7.setText(_translate("EmployeeRetention", "Enter education (rating from 0 - 5):"))
        self.label_8.setText(_translate("EmployeeRetention", "Enter the education field:"))
        self.label_9.setText(_translate("EmployeeRetention", "Enter the environment satisfaction (rating from 0 - 5):"))
        self.label_10.setText(_translate("EmployeeRetention", "Enter gender:"))
        self.label_11.setText(_translate("EmployeeRetention", "Enter hourly rate:"))
        self.label_12.setText(_translate("EmployeeRetention", "Enter Job involvement (rating from 0 - 5):"))
        self.label_13.setText(_translate("EmployeeRetention", "Enter Job level (rating from 0 - 5):"))
        self.label_14.setText(_translate("EmployeeRetention", "Enter job role:"))
        self.label_15.setText(_translate("EmployeeRetention", "Enter Job satisfaction(rating from 0 - 5):"))
        self.label_16.setText(_translate("EmployeeRetention", "Enter marital status:"))
        self.label_17.setText(_translate("EmployeeRetention", "Enter monthly income:"))
        self.label_18.setText(_translate("EmployeeRetention", "Enter monthly rate:"))
        self.label_19.setText(_translate("EmployeeRetention", "Enter no. of companies worked:"))
        self.label_20.setText(_translate("EmployeeRetention", "Enter overtime ( yes/no):"))
        self.label_21.setText(_translate("EmployeeRetention", "Enter the percent of salary hike (out of 100):"))
        self.label_22.setText(_translate("EmployeeRetention", "Enter performance rating (rating from 0 -5):"))
        self.label_23.setText(_translate("EmployeeRetention", "Enter relationship satisfaction (rating from 0-5):"))
        self.label_24.setText(_translate("EmployeeRetention", "Enter total woking years:"))
        self.label_25.setText(_translate("EmployeeRetention", "Enter the training times last year:"))
        self.label_26.setText(_translate("EmployeeRetention", "Enter work life balance (rating from 0-5):"))
        self.label_27.setText(_translate("EmployeeRetention", "Enter years at the company:"))
        self.label_28.setText(_translate("EmployeeRetention", "Enter years at current role:"))
        self.label_29.setText(_translate("EmployeeRetention", "Enter years since last promotion:"))
        self.label_30.setText(_translate("EmployeeRetention", "Enter years with current manager:"))

        self.csv_open.setText(_translate("EmployeeRetention", "Open"))
        self.label.setText(_translate("EmployeeRetention", "Open a .csv file "))
        self.submit.setText(_translate("EmployeeRetention", "Submit"))
        self.save.setText(_translate("EmployeeRetention", "Save"))

    check_list = []

    def open_csv(self):
        global filename, Data
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(EmployeeRetention, 'Open file', 'c:\\', "CSV files (*.csv)")
        with open(filename, 'r') as file:
            Reader = csv.reader(file)
            Data = list(Reader)
            del (Data[0])
            self.listbox1.clear()
            self.check_list.clear()
            for x in list(range(0, len(Data))):
                self.listbox1.addItem(Data[x][0])
                self.check_list.append(Data[x][0])
        file.close()

    def update(self):
        index = self.listbox1.selectedItems()[0].text()
        for i in self.check_list:
            if i == index:
                index = self.check_list.index(i)
        self.el1.setText(Data[index][1])
        self.el2.setCurrentIndex(self.el2.findText(Data[index][2]))
        self.el3.setText(Data[index][3])
        self.el4.setCurrentIndex(self.el4.findText(Data[index][4]))
        self.el5.setText(Data[index][5])
        self.el6.setText(Data[index][6])
        self.el7.setCurrentIndex(self.el7.findText(Data[index][7]))
        self.el8.setText(Data[index][8])
        self.el9.setCurrentIndex(self.el9.findText(Data[index][9]))
        self.el10.setText(Data[index][10])
        self.el11.setText(Data[index][11])
        self.el12.setText(Data[index][12])
        self.el13.setCurrentIndex(self.el13.findText(Data[index][13]))
        self.el14.setText(Data[index][14])
        self.el15.setCurrentIndex(self.el15.findText(Data[index][15]))
        self.el16.setText(Data[index][16])
        self.el17.setText(Data[index][17])
        self.el18.setText(Data[index][18])
        self.el19.setCurrentIndex(self.el19.findText(Data[index][19]))
        self.el20.setText(Data[index][20])
        self.el21.setText(Data[index][21])
        self.el22.setText(Data[index][22])
        self.el23.setText(Data[index][23])
        self.el24.setText(Data[index][24])
        self.el25.setText(Data[index][25])
        self.el26.setText(Data[index][26])
        self.el27.setText(Data[index][27])
        self.el28.setText(Data[index][28])
        self.el29.setText(Data[index][29])

    def save_entry_data(self):
        save = []
        save.append(int(self.el1.text()))
        save.append(self.el2.currentText())
        save.append(int(self.el3.text()))
        save.append(self.el4.currentText())
        save.append(int(self.el5.text()))
        save.append(int(self.el6.text()))
        save.append(self.el7.currentText())
        save.append(int(self.el8.text()))
        save.append(self.el9.currentText())
        save.append(int(self.el10.text()))
        save.append(int(self.el11.text()))
        save.append(int(self.el12.text()))
        save.append(self.el13.currentText())
        save.append(int(self.el14.text()))
        save.append(self.el15.currentText())
        save.append(int(self.el16.text()))
        save.append(int(self.el17.text()))
        save.append(int(self.el18.text()))
        save.append(self.el19.currentText())
        save.append(int(self.el20.text()))
        save.append(int(self.el21.text()))
        save.append(int(self.el22.text()))
        save.append(int(self.el23.text()))
        save.append(int(self.el24.text()))
        save.append(int(self.el25.text()))
        save.append(int(self.el26.text()))
        save.append(int(self.el27.text()))
        save.append(int(self.el28.text()))
        save.append(int(self.el29.text()))
        self.name = QtWidgets.QInputDialog.getText(EmployeeRetention, 'Please provide the employee name',
                                                   'Enter ther name:')
        save.insert(0, self.name[0])
        with open(filename, 'a') as f:
            write = csv.writer(f, lineterminator='\n')
            write.writerow(save)
            f.close()

    def get_entry_data(self):
        business_travel = 3
        dept = 3
        edu_field = 3
        gender = 3
        job_role = 3
        martital = 3
        over_time = 3

        age = int(self.el1.text())

        if self.el2.currentText() == "Non Travel":
            business_travel = 0
        elif self.el2.currentText() == "Travel Frequently":
            business_travel = 1
        elif self.el2.currentText() == "Travel Rarely":
            business_travel = 2

        daily_rate = int(self.el3.text())

        if self.el4.currentText() == "Human Resources":
            dept = 0
        elif self.el4.currentText() == "Research & Development":
            dept = 1
        elif self.el4.currentText() == "Sales":
            dept = 2

        dist_home = int(self.el5.text())

        education = int(self.el6.text())

        if self.el7.currentText() == "Human Resources":
            edu_field = 0
        elif self.el7.currentText() == "Life Sciences":
            edu_field = 1
        elif self.el7.currentText() == "Marketing":
            edu_field = 2
        elif self.el7.currentText() == "Medical":
            edu_field = 3
        elif self.el7.currentText() == "Other":
            edu_field = 4

        Environment_satification = int(self.el8.text())

        if self.el9.currentText() == "Female":
            gender = 0
        elif self.el9.currentText() == "Male":
            gender = 1

        Hourly_rate = int(self.el10.text())

        job_invol = int(self.el11.text())

        job_level = int(self.el12.text())

        if self.el13.currentText() == "Health Care Representative":
            job_role = 0
        elif self.el13.currentText() == "Human Resources":
            job_role = 1
        elif self.el13.currentText() == "Laboratory Technician":
            job_role = 2
        elif self.el13.currentText() == "Manager":
            job_role = 3
        elif self.el13.currentText() == "Manufacturing Director":
            job_role = 4
        elif self.el13.currentText() == "Research Director":
            job_role = 5
        elif self.el13.currentText() == "Research Scientist":
            job_role = 6
        elif self.el13.currentText() == "Sales Executive":
            job_role = 7

        job_satisifaction = int(self.el14.text())

        if self.el15.currentText() == "Single":
            martital = 0
        elif self.el15.currentText() == "Divorced":
            martital = 1
        elif self.el15.currentText() == "Married":
            martital = 2

        monthly_income = int(self.el16.text())

        monthly_rate = int(self.el17.text())

        num_company = int(self.el18.text())

        if self.el19.currentText() == "No":
            over_time = 0
        elif self.el19.currentText() == "Yes":
            over_time = 1

        salary_hike = int(self.el20.text())

        performance_rate = int(self.el21.text())

        relationship_satisfaction = int(self.el22.text())

        total_work_years = int(self.el23.text())

        training_time = int(self.el24.text())

        work_life_bal = int(self.el25.text())

        year_at_company = int(self.el26.text())

        year_in_role = int(self.el27.text())

        last_promotion = int(self.el28.text())

        current_manager = int(self.el29.text())

        y_pred = []
        labels = [age, business_travel, daily_rate, dept, dist_home, education, edu_field, Environment_satification,
                  gender, Hourly_rate,
                  job_invol, job_level, job_role, job_satisifaction, martital, monthly_income, monthly_rate,
                  num_company, over_time, salary_hike,
                  performance_rate, relationship_satisfaction, total_work_years, training_time, work_life_bal,
                  year_at_company, year_in_role, last_promotion, current_manager]
        for i in labels:
            y_pred.append(i)
        y_pred = np.reshape(y_pred, (1, -1))

        log_reg = joblib.load("trained_model")

        txt = log_reg.predict(y_pred)

        if txt == 0:
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Employee Retention System")
            self.msg.setInformativeText("Employee will stay")
            self.msg.setWindowTitle("ERS")
            self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msg.exec_()
        else:
            self.msg.setIcon(QtWidgets.QMessageBox.Warning)
            self.msg.setText("Employee Retention System")
            self.msg.setInformativeText("Chances of this employee to leave the job is high")
            self.msg.setWindowTitle("ERS")
            self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    EmployeeRetention = QtWidgets.QMainWindow()
    ui = Ui_EmployeeRetention()
    ui.setupUi(EmployeeRetention)
    EmployeeRetention.show()
    sys.exit(app.exec_())