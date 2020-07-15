from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractScrollArea, QVBoxLayout, QWidget

from Alf import *
import re

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalysisFreq(object):

    def setupUi(self, AnalysisFreq):
        AnalysisFreq.setObjectName("AnalysisFreq")
        AnalysisFreq.resize(672, 600)
        AnalysisFreq.setMinimumSize(QtCore.QSize(672, 600))
        AnalysisFreq.setMaximumSize(QtCore.QSize(672, 600))
        self.centralwidget = QtWidgets.QWidget(AnalysisFreq)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 530, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 530, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 410, 651, 97))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 672, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 210, 672, 191))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        AnalysisFreq.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnalysisFreq)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 22))
        self.menubar.setObjectName("menubar")
        AnalysisFreq.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnalysisFreq)
        self.statusbar.setObjectName("statusbar")
        AnalysisFreq.setStatusBar(self.statusbar)

        self.retranslateUi(AnalysisFreq)
        QtCore.QMetaObject.connectSlotsByName(AnalysisFreq)


    def retranslateUi(self, AnalysisFreq):
        _translate = QtCore.QCoreApplication.translate
        AnalysisFreq.setWindowTitle(_translate("AnalysisFreq", "Analysis"))
        self.pushButton.setText(_translate("AnalysisFreq", "Стандартная замена"))
        self.pushButton_3.setText(_translate("AnalysisFreq", "Запуск"))

    def paintPlot(self, Layout ,x, y):
        import matplotlib
        matplotlib.rcParams.update({'font.size': 5.5})

        self.figure = plt.figure(figsize=(6.6,1.9))
        self.canvas = FigureCanvas(self.figure)

        Layout.addWidget(self.canvas)

        ax = self.figure.add_subplot()
        ax.bar(x,y)
        ax.grid()
        y_ticks = []
        last = 0
        for y_ in y:
            if abs(y_ - last) > 0.6:
                y_ticks.append(y_)
                last = y_
        plt.yticks(y_ticks)


        self.canvas.draw()



def choice_alf (text):
    res = ''.join(re.findall('[A-Za-zА-Яа-яёЁ]', text))
    if res[0].lower() in alf1: return alf1,len(res)
    elif res[0].lower() in alf3: return alf3,len(res)

def freq_ch(text):
    array = dict([])
    alf,len_text = choice_alf(text)

    text = list(text)
    for ch in alf:
        array.update([(ch, round((text.count(ch.lower())+text.count(ch.upper()))/len_text*100,2))])
    return array


def sort_freq(freq_text):
    return({key: value for key, value in sorted(freq_text.items(), key=lambda item: item[1], reverse=True)})

def text_to_table(table,text,str):
    i=0
    for ch in text:
        item = QTableWidgetItem(ch)
        if str == 0:item.setFlags(QtCore.Qt.ItemIsEnabled)
        table.setItem(str, i, item)
        i+=1

def table_to_text(table,str):
    array = []
    for i in range(table.columnCount()):
        array.append(table.model().index(str,i).data())
    return array

def decrypt(text,array_ch,new_ch):
    result = []

    for ch in text:
        if ch.lower() in array_ch and new_ch[array_ch.index(ch.lower())] != None:
            if ch.islower():result.append(new_ch[array_ch.index(ch.lower())])
            else: result.append(new_ch[array_ch.index(ch.lower())].upper())
        else: result.append(ch)


    return ''.join(result)
