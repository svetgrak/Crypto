# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")

        mainWindow.resize(600, 450)
        mainWindow.setMaximumSize(QtCore.QSize(600, 450))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 350, 17))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 350, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 350, 121, 31))
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Crypto"))
        self.label.setText(_translate("mainWindow", "Выберите алгоритм :"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Атбаш"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Сцитала"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Цезарь"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Квадрат Полибия"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Кардано"))
        self.comboBox.setItemText(5, _translate("mainWindow", "Ришелье"))
        self.comboBox.setItemText(6, _translate("mainWindow", "Диск Альберти"))
        self.comboBox.setItemText(7, _translate("mainWindow", "Гронсфельд"))
        self.comboBox.setItemText(8, _translate("mainWindow", "Виженер"))
        self.comboBox.setItemText(9, _translate("mainWindow", "Плейфер"))
        self.comboBox.setItemText(10, _translate("mainWindow", "Криптосистема Хилла"))
        self.comboBox.setItemText(11, _translate("mainWindow", "Вернам"))
        self.comboBox.setItemText(12, _translate("mainWindow", "Метод гаммирования"))
        self.comboBox.setItemText(13, _translate("mainWindow", "Частотный криптоанализ"))
        self.comboBox.setItemText(14, _translate("mainWindow", "Криптоанализ полиалфавитных шифров"))
        self.comboBox.setItemText(15, _translate("mainWindow", "DES"))
        self.pushButton.setText(_translate("mainWindow", "Далее"))
