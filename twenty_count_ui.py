# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twenty_count_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(778, 397)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sub.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("tracyhead.jpg"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 4)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "24计算"))
        self.pushButton.setText(_translate("dialog", "tracy来算~"))
