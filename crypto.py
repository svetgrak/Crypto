from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog, qApp, QHeaderView,QTableWidgetItem
from mainWindow import Ui_mainWindow
from Cypher import Window
from Analysis import Ui_Analysis
from new_form import Ui_form
import Atbash
import Scytale
import Caesar
import Polybius
import Cardan
import Rishele
import Alberti
import Gronsf
import Vigenere
import Playfair
import Hill
import Vernam
import Gamma_cypher
import AnalysisFreq
import AnalysisPolyAlf

import sys
from Alf import *

class AddWindowForFreq(QMainWindow, AnalysisFreq.Ui_AnalysisFreq):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def AnalysisFr(self,text):

        freq_text = AnalysisFreq.sort_freq(AnalysisFreq.freq_ch(text))

        if len(freq_text) == 26: standart_freq = AnalysisFreq.sort_freq(standart_freq_en)
        else: standart_freq = AnalysisFreq.sort_freq(standart_freq_rus)
        self.addWin.tableWidget.setColumnCount(len(freq_text))
        self.addWin.tableWidget.setRowCount(2)
        AnalysisFreq.text_to_table(self.addWin.tableWidget, list(freq_text.keys()), 0)
        self.addWin.tableWidget.resizeColumnsToContents()

        def Standart():
            AnalysisFreq.text_to_table(self.addWin.tableWidget, list(standart_freq.keys()), 1)

        self.addWin.paintPlot(self.addWin.formLayout, list(freq_text.keys()), list(freq_text.values()))
        self.addWin.paintPlot(self.addWin.formLayout_2, list(standart_freq.keys()), list(standart_freq.values()))
        self.addWin.pushButton.clicked.connect(Standart)

    def decrypt(self):
        self.ui.textEdit_2.setText(AnalysisFreq.text_to_table())


class AddWindowForPolyAlf(QMainWindow, AnalysisPolyAlf.Ui_AnalysisPolyAlf):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def MethIC(self,text,min_ic):

        forTable = (AnalysisPolyAlf.methodIndex(text,float(min_ic)))

        self.addWin.tableWidget.setRowCount(len(forTable[0]))
        for i in range(len(forTable[0])):
            item = QTableWidgetItem(str(i+1))
            item2 = QTableWidgetItem(str(forTable[0][i]))
            item3 = QTableWidgetItem(str(forTable[1][i]))
            item4 = QTableWidgetItem(str(forTable[2][i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget.setItem(i, 0, item)
            self.addWin.tableWidget.setItem(i, 1, item2)
            self.addWin.tableWidget.setItem(i, 2, item3)
            self.addWin.tableWidget.setItem(i, 3, item4)
            #self.addWin.tableWidget.resizeColumnsToContents()

    def PrintKeysFor1(self):
        text = self.ui.textEdit.toPlainText()
        indexes = []
        for i in range(self.addWin.tableWidget.rowCount()):
            indexes.append(self.addWin.tableWidget.model().index(i,3).data())
        indexes[0] = 0
        keys = AnalysisPolyAlf.printKeyFor1(text,indexes)
        self.addWin.tableWidget_2.setRowCount(len(keys))
        for i in range(len(keys)):
            item = QTableWidgetItem(str(keys[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget_2.setItem(i, 0, item)

    def PrintKeysFor2(self):
        text = self.ui.textEdit.toPlainText()
        indexes = []
        for i in range(self.addWin.tableWidget_6.rowCount()):
            indexes.append(self.addWin.tableWidget_6.model().index(i, 0).data())

        keys = AnalysisPolyAlf.printKeyFor2(text, indexes)
        self.addWin.tableWidget_5.setRowCount(len(keys))
        for i in range(len(keys)):
            item = QTableWidgetItem(str(keys[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget_5.setItem(i, 0, item)

    def MethKasis(self,text,count_symb):
        result = AnalysisPolyAlf.methodKasiski(text,count_symb)
        len_keys, freq_keys = list(result[1].keys()),list(result[1].values())
        double, count_double = list(result[0].keys()),list(result[0].values())


        self.addWin.tableWidget_3.setRowCount(len(double))
        for i in range(len(double)):
            doub = QTableWidgetItem(str(double[i]))
            count_doub = QTableWidgetItem(str(count_double[i]))
            doub.setFlags(QtCore.Qt.ItemIsEnabled)
            count_doub.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget_3.setItem(i, 0, doub)
            self.addWin.tableWidget_3.setItem(i, 1, count_doub)

        self.addWin.tableWidget_4.setRowCount(len(len_keys))
        for i in range(len(len_keys)):
            len_key = QTableWidgetItem(str(len_keys[i]))
            freq_key = QTableWidgetItem(str(freq_keys[i]))
            len_key.setFlags(QtCore.Qt.ItemIsEnabled)
            freq_key.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget_4.setItem(i, 0, len_key)
            self.addWin.tableWidget_4.setItem(i, 1, freq_key)
        return

    def PrintPlotAutoCorel(self,text):
        x = AnalysisPolyAlf.plot(text)
        AnalysisPolyAlf.paintPlot(self,self.addWin.gridLayout,x)
        return

    def MethAutoCorrel(self,text):

        len_key = self.addWin.lineEdit_3.text()
        if len_key  == '' or len_key .isdigit() == False: msgShow("Введите предполагаемую длину ключа")
        else:
            indexes = AnalysisPolyAlf.methodAutoCorrel(text,int(len_key))
            self.addWin.tableWidget_6.setRowCount(len(indexes))
            for i in range(len(indexes)):
                item = QTableWidgetItem(str(indexes[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.addWin.tableWidget_6.setItem(0, i, item)


class MainWin(QMainWindow):

    def __init__(self):
        super(MainWin,self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenNextWindow)

    def OpenNextWindow(self):
        choice = str(self.ui.comboBox.currentText())
        self.ui = Window()
        self.ui.setupUi(self)

        if choice == 'Атбаш':
            self.ui.label_4.setText('Шифр Атбаш')
            self.ui.lineEdit_2.hide()
            self.ui.label_2.hide()
            self.ui.pushButton.clicked.connect(self.AtbashEncrypt)
            self.ui.pushButton_2.clicked.connect(self.AtbashDecrypt)

        elif choice == 'Сцитала':
            self.ui.label_4.setText('Шифр Сцитала')
            self.ui.label_2.setText("Ключ (число): ")
            self.ui.pushButton.clicked.connect(self.ScytaleEncrypt)
            self.ui.pushButton_2.clicked.connect(self.ScytaleDecrypt)

        elif choice == 'Цезарь':
            self.ui.label_4.setText('Шифр Цезаря')
            self.ui.label_2.setText("Ключ (число): ")
            self.ui.pushButton.clicked.connect(self.CaesarEncrypt)
            self.ui.pushButton_2.clicked.connect(self.CaesarDecrypt)

        elif choice == 'Квадрат Полибия':
            self.ui.label_4.setText('Квадрат Полибия')
            self.ui.label_2.setText("Ключ (текст): ")
            self.ui.pushButton.clicked.connect(self.PolybiusEncrypt)
            self.ui.pushButton_2.clicked.connect(self.PolybiusDecrypt)

        elif choice == 'Кардано':

            self.ui.label_4.setText('Шифр Кардано')
            self.ui.label_2.setText("Ключ в формате (1 2 ... 10 11 и т.д): ")
            self.ui.pushButton_3.show()
            self.ui.pushButton_4.show()
            self.ui.pushButton_5.show()
            self.ui.pushButton.clicked.connect(self.CardanEncrypt)
            self.ui.pushButton_2.clicked.connect(self.CardanDecrypt)
            self.ui.pushButton_3.clicked.connect(self.CardanKeyGen)
            self.ui.pushButton_4.clicked.connect(self.InFile)
            self.ui.pushButton_5.clicked.connect(self.OfFile)

        elif choice == 'Ришелье':
            self.ui.label_4.setText('Шифр Ришелье')
            self.ui.label_2.setText("Ключ (например (213)(123)(21)(321), количество букв в блоке < 10 ): ")
            self.ui.pushButton_3.show()
            self.ui.pushButton_4.show()
            self.ui.pushButton_5.show()
            self.ui.pushButton.clicked.connect(self.RisheleEncrypt)
            self.ui.pushButton_2.clicked.connect(self.RisheleDecrypt)
            self.ui.pushButton_3.clicked.connect(self.RisheleKeyGen)
            self.ui.pushButton_4.clicked.connect(self.InFile)
            self.ui.pushButton_5.clicked.connect(self.OfFile)

        elif choice == 'Диск Альберти':
            self.ui.pushButton_3.show()
            self.ui.pushButton_4.show()
            self.ui.pushButton_5.show()
            self.ui.label_5.show()
            self.ui.lineEdit_4.show()
            self.ui.label_4.setText('Диск Альберти')
            self.ui.label_5.setText("Ключ (текст): ")
            self.ui.label_2.setText("Ключ для таблицы: ")
            self.ui.pushButton_3.setText("Сгенерировать доп ключ")
            self.ui.pushButton_4.setText("Сохранить доп ключ")
            self.ui.pushButton_5.setText("Загрузить доп ключ")
            self.ui.pushButton.clicked.connect(self.AlbertiEncrypt)
            self.ui.pushButton_2.clicked.connect(self.AlbertiDecrypt)
            self.ui.pushButton_3.clicked.connect(self.AlbertiKeyGen)
            self.ui.pushButton_4.clicked.connect(self.InFile)
            self.ui.pushButton_5.clicked.connect(self.OfFile)

        elif choice == 'Гронсфельд':
            self.ui.label_4.setText('Шифр Гронсфельда')
            self.ui.label_2.setText("Ключ (число): ")
            self.ui.pushButton.clicked.connect(self.GronsfeldEncrypt)
            self.ui.pushButton_2.clicked.connect(self.GronsfeldDecrypt)

        elif choice == 'Виженер':
            self.ui.label_4.setText('Шифр Виженера')
            self.ui.label_2.setText('Ключ (текст): ')
            self.ui.pushButton.clicked.connect(self.VigenereEncrypt)
            self.ui.pushButton_2.clicked.connect(self.VigenereDecrypt)

        elif choice == 'Плейфер':
            self.ui.label_4.setText('Шифр Плейфера')
            self.ui.label_2.setText('Ключ(текст): ')
            self.ui.pushButton.clicked.connect(self.PlayfairEncrypt)
            self.ui.pushButton_2.clicked.connect(self.PlayfairDecrypt)

        elif choice == 'Криптосистема Хилла':
            self.ui.label_4.setText('Криптосистема Хилла')
            self.ui.label_2.setText('Ключ (текст длина = квадрату целого числа (9,16,25 и т.д.): ')
            self.ui.pushButton.clicked.connect(self.HillEncrypt)
            self.ui.pushButton_2.clicked.connect(self.HillDecrypt)

        elif choice == 'Вернам':
            self.ui.label_4.setText('Шифр Вернама')
            self.ui.label_2.setText('Двоичная гамма: ')
            self.ui.pushButton_3.show()
            self.ui.pushButton_4.show()
            self.ui.pushButton_5.show()
            self.ui.pushButton_3.setText("Сгенерировать двоичную гамму")
            self.ui.pushButton_4.setText("Сохранить гамму")
            self.ui.pushButton_5.setText("Загрузить гамму")
            self.ui.pushButton.clicked.connect(self.VernamEncrypt)
            self.ui.pushButton_2.clicked.connect(self.VernamDecrypt)
            self.ui.pushButton_3.clicked.connect(self.VernamGammaGen)
            self.ui.pushButton_4.clicked.connect(self.InFile)
            self.ui.pushButton_5.clicked.connect(self.OfFile)
            msgShow(
                'При работе с английским алфавитом могут возникнуть проблемы с регистром. Обусловлено тем, что пришлось добивать алфавит до 32 '
                'символов такими символами как .,!?(), а у них регистра нет. поэтому при расшифровке изначальные символы будут в высоком регистре')

        elif choice == 'Метод гаммирования':
            self.ui.label_4.setText('Шифрование методом гаммирования')
            self.ui.label_2.setText('Гамма (текст) длина гаммы не больше длины текста: ')
            self.ui.pushButton_3.show()
            self.ui.pushButton_4.show()
            self.ui.pushButton_5.show()
            self.ui.pushButton_3.setText("Сгенерировать гамму")
            self.ui.pushButton_4.setText("Сохранить гамму")
            self.ui.pushButton_5.setText("Загрузить гамму")
            self.ui.pushButton.clicked.connect(self.GammaEncrypt)
            self.ui.pushButton_2.clicked.connect(self.GammaDecrypt)
            self.ui.pushButton_3.clicked.connect(self.GammaGen)
            self.ui.pushButton_4.clicked.connect(self.InFile)
            self.ui.pushButton_5.clicked.connect(self.OfFile)
            msgShow(
                'Гамма вырабатывается линейным конгруэнтным методом и сразу представляется в виде символов алфавита сообщения для шифрования')

        elif choice == 'Частотный криптоанализ':
            self.ui = Ui_Analysis()
            self.ui.setupUi(self)
            self.ui.retranslateUi(self,name="Freq")

            self.ui.action.setStatusTip("Загрузить шифротекст из файла")
            self.ui.action_2.setStatusTip("Сохранить результат в файл")
            self.ui.action.triggered.connect(self.OfFileOfTextEdit)
            self.ui.action_2.triggered.connect(self.InFileOfTextEdit)
            self.ui.pushButton.clicked.connect(self.OpenAnalysisFreq)
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.hide()
            #self.ui.action_3.triggered.connect(self.back)
            #self.ui.action_3.setStatusTip("Вернуться к выбору алгоритма ")

        elif choice == 'Криптоанализ полиалфавитных шифров':
            self.ui = Ui_Analysis()
            self.ui.setupUi(self)
            self.ui.retranslateUi(self, name="Poly")
            self.ui.action.setStatusTip("Загрузить шифротекст из файла")
            self.ui.action_2.setStatusTip("Сохранить результат в файл")
            self.ui.action.triggered.connect(self.OfFileOfTextEdit)
            self.ui.action_2.triggered.connect(self.InFileOfTextEdit)
            self.ui.pushButton.setText('Рассчитать ключ')
            self.ui.pushButton.clicked.connect(self.OpenPolyAlfAnalysis)

        elif choice == "DES":
            self.ui = Ui_form()
            self.ui.setupUi(self)
            self.ui.retranslateUi(self)





    def AtbashEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else: self.ui.lineEdit_3.setText(Atbash.enc(text))

    def AtbashDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else: self.ui.lineEdit_3.setText(Atbash.dec(text))

    def ScytaleEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isdigit() == False or int(key) == 0 or int(key)>len(text): msgShow("Ключ должен быть натуральным числом и не больше длины текста")
            else: self.ui.lineEdit_3.setText(Scytale.enc(text,int(key)))

    def ScytaleDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isdigit() == False or int(key) == 0: msgShow("Ключ должен быть натуральным числом")
            else:self.ui.lineEdit_3.setText(Scytale.dec(text, int(key)))

    def CaesarEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if (key[0] == '-' and key[1:].isdigit() == True) or key.isdigit() == True: self.ui.lineEdit_3.setText(Caesar.enc(text, int(key)))
            else: msgShow("Ключ должен быть числом")

    def CaesarDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isdigit() == False or int(key) == 0: msgShow("Ключ должен быть натуральным числом")
            else: self.ui.lineEdit_3.setText(Caesar.dec(text, int(key)))

    def PolybiusEncrypt(self):
        text = self.ui.lineEdit.text()
        if text =='': msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() == True or key == '': self.ui.lineEdit_3.setText(Polybius.enc(text,key))
            else: msgShow("Ключ должен быть текстом")

    def PolybiusDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() == True or key == '': self.ui.lineEdit_3.setText(Polybius.dec(text,key))
            else: msgShow("Ключ должен быть текстом")

    def InFile(self):
        text = self.ui.lineEdit_2.text()
        if text != '':
            while True:
                choice, ok = QInputDialog.getText(self, 'File name ', 'input File name')
                if ok and choice != '':
                    file = open(choice,'w')
                    msgShow("Сохранение произошло успешно!")
                    file.write(text)
                    file.close()
                    break
                else:
                    msgShow("Сохранение не произошло.")
                    break

        else: msgShow("Введите или сгенерируйте ключ")

    def OfFile(self):
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '','*',)[0]
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.ui.lineEdit_2.setText(data)
            f.close()

    def InFileOfTextEdit(self):
        text = self.ui.textEdit_2.toPlainText()
        if text != '':
            while True:
                choice, ok = QInputDialog.getText(self, 'File name ', 'input File name')
                if ok and choice != '':
                    file = open(choice, 'w')
                    msgShow("Сохранение произошло успешно!")
                    file.write(text)
                    file.close()
                    break
                else:
                    msgShow("Сохранение не произошло.")
                    break

        else:
            msgShow("Введите текст для сохранения")

    def OfFileOfTextEdit(self):
        fname = QFileDialog.getOpenFileName(self, 'OpenFile', '', '*', )[0]
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.ui.textEdit.setText(data)
            f.close()

    def CardanKeyGen(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow("Введите данные для шифрования.")
        else:
            self.ui.lineEdit_2.setText(Cardan.KeyForCardan(text))
            msgShow("Не забудь сохранить ключ.")

    def CardanEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow("Введите данные")
        else:
            key = self.ui.lineEdit_2.text()
            if key == '': msgShow("Введите или сгенерируйте ключ")
            elif Cardan.checkKey(text,key) == False: msgShow("Введите правильный ключ")
            else: self.ui.lineEdit_3.setText(Cardan.enc(text,key))

    def CardanDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow("Введите данные")
        else:
            key = self.ui.lineEdit_2.text()
            if key == '': msgShow("Введите или загрузите ключ")
            else: self.ui.lineEdit_3.setText(Cardan.dec(text, key))

    def RisheleKeyGen(self):
        lenText = len(self.ui.lineEdit.text())
        if lenText != 0: self.ui.lineEdit_2.setText(Rishele.KeyForRishele(lenText))
        else: msgShow("Введите текст для шифрования.")

    def RisheleEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите текст для шифрования')
        else:
            key = self.ui.lineEdit_2.text()
            if key == '':msgShow('Введите или сгенерируйте ключ.')
            else:
                if Rishele.checkKey(text,key): self.ui.lineEdit_3.setText(Rishele.enc(text,key))
                else: msgShow("Введите верный ключ заданного формата")

    def RisheleDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':
            msgShow('Введите текст для шифрования')
        else:
            key = self.ui.lineEdit_2.text()
            if key == '': msgShow('Введите или сгенерируйте ключ.')
            else:
                if Rishele.checkKey(text,key): self.ui.lineEdit_3.setText(Rishele.dec(text, key))
                else:msgShow("Введите верный ключ заданного формата")

    def GronsfeldEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':
            msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isdigit() == False or int(key) == 0 or len(key) > len(text):
                msgShow("Ключ должен быть натуральным числом и длина ключа не больше длины текста")
            else:
                key *= len(text)//len(key)+1
                self.ui.lineEdit_3.setText(Gronsf.enc(text,key))

    def GronsfeldDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':
            msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isdigit() == False or int(key) == 0 or len(key) > len(text):
                msgShow("Ключ должен быть натуральным числом и длина ключа не больше длины текста")
            else: self.ui.lineEdit_3.setText(Gronsf.dec(text,key))

    def AlbertiKeyGen(self):

        while (True) :
            choice,ok = QInputDialog.getText(self, 'Choice alphabet','rus - russian, en - english')
            if choice == 'rus' :
                key = Alberti.KeyForAlberti_Rus()
                break
            if choice == 'en':
                key = Alberti.KeyForAlberti_En()
                break
            if ok == False: break

        self.ui.lineEdit_2.setText(key)
        msgShow("Не забудьте сохранить ключ.")

    def AlbertiEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_4.text()
            keyForTable = self.ui.lineEdit_2.text()
            if key.isalpha() != True: msgShow("Ключ должен быть текстом")
            elif keyForTable == '':msgShow("Введите либо сгенерируйте дополнительный ключ")
            elif keyForTable.isalpha()!= True: msgShow("Дополнительный ключ должен быть текстом")
            else: self.ui.lineEdit_3.setText(Alberti.enc(text,key,keyForTable))

    def AlbertiDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_4.text()
            keyForTable = self.ui.lineEdit_2.text()
            if key.isalpha() != True: msgShow("Ключ должен быть текстом")
            elif keyForTable == '': msgShow("Введите либо загрузите дополнительный ключ")
            elif keyForTable.isalpha() != True: msgShow("Дополнительный ключ должен быть текстом")
            else: self.ui.lineEdit_3.setText(Alberti.dec(text, key, keyForTable))

    def VigenereEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key == '': msgShow("Введите ключ")
            elif key.isalpha() != True: msgShow("Ключ должен быть текстом")
            elif len(key)> len(text): msgShow("Длина ключа должна быть не больше длины текста")
            else: self.ui.lineEdit_3.setText(Vigenere.enc(text,key))

    def VigenereDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() != True or key == '': msgShow("Ключ должен быть текстом")
            elif len(key) > len(text): msgShow("Длина ключа должна быть не больше длины текста")
            else: self.ui.lineEdit_3.setText(Vigenere.dec(text, key))

    def PlayfairEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() != True or key == '':msgShow("Ключ должен быть текстом")
            elif len(key) > len(text):msgShow("Длина ключа должна быть не больше длины текста")
            else:self.ui.lineEdit_3.setText(Playfair.enc(text, key))

    def PlayfairDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() != True or key == '':msgShow("Ключ должен быть текстом")
            elif len(key) > len(text):msgShow("Длина ключа должна быть не больше длины текста")
            else:self.ui.lineEdit_3.setText(Playfair.dec(text, key))

    def HillEncrypt(self):
        text = self.ui.lineEdit.text()
        if text =='':msgShow('Введите данные')
        elif Hill.check_text(text) == False: msgShow('Введите символы из алфавита: '+'\n'
                                                     'для англ: a-z A-Z, а также доп символы ".", ",", " " '+'\n'
                                                     'для русского: а-я А-Я, а также доп символы ".", ",", "?", " "')

        else:
            key = self.ui.lineEdit_2.text()
            check = Hill.check_key(key)
            if key.isalpha()!=True or key == '': msgShow("Ключ должен быть текстом")
            elif check[1] != 2 and check[0] == True:
                result = Hill.enc(text,key)
                if result == 'Key is wrong': msgShow("К сожалению шифрование с этим ключом невозможно. Поменяйте ключ.")
                else: self.ui.lineEdit_3.setText(result)
            else: msgShow('Длина ключа должна быть 9, 16, 25 и т.д.')

    def HillDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() != True or key == '':msgShow("Ключ должен быть текстом")
            elif Hill.check_key(key)[0]:self.ui.lineEdit_3.setText(Hill.dec(text, key))
            else:msgShow('Длина ключа должна быть квадратом целого числа')

    def VernamGammaGen(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите текст для которого сгенерировать гамму: ')
        else: self.ui.lineEdit_2.setText(Vernam.gamma_gen(text))

    def VernamEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите текст для шифрования')
        else:
            gamma = self.ui.lineEdit_2.text()
            if gamma == '': msgShow('Введите или сгенерируйте двоичную гамму')
            else:
                if len(gamma) == len(text)*5: self.ui.lineEdit_3.setText(Vernam.enc(text,gamma))
                else: msgShow('Гамма не походит для шифруемого текста')

    def VernamDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите текст для шифрования')
        else:
            gamma = self.ui.lineEdit_2.text()
            if gamma == '':msgShow('Введите или загрузите двоичную гамму')
            else:
                if len(gamma) == len(text)*5: self.ui.lineEdit_3.setText(Vernam.dec(text, gamma))
                else:msgShow('Гамма не походит для шифруемого текста')

    def GammaGen(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите текст для которого сгенерировать гамму: ')
        else:
            if text[1] in alf1 or alf2:self.ui.lineEdit_2.setText(Gamma_cypher.gamma_gen_rus(text))
            elif text[1] in alf2 or alf4:self.ui.lineEdit_2.setText(Gamma_cypher.gamma_gen_en(text))
            else: msgShow('возникла непредвиденная ошибка')

    def GammaEncrypt(self):
        text = self.ui.lineEdit.text()
        if text == '': msgShow('Введите текст для шифрования')
        else:
            gamma = self.ui.lineEdit_2.text()
            if gamma == '': msgShow('Введите или сгенерируйте гамму')
            else:
                if len(gamma) == len(text):
                    self.ui.lineEdit_3.setText(Gamma_cypher.enc(text, gamma))
                else:msgShow('Гамма не походит для шифруемого текста')

    def GammaDecrypt(self):
        text = self.ui.lineEdit.text()
        if text == '':msgShow('Введите текст для шифрования')
        else:
            gamma = self.ui.lineEdit_2.text()
            if gamma == '':msgShow('Введите или загрузите гамму')
            else:
                if len(gamma) == len(text):self.ui.lineEdit_3.setText(Gamma_cypher.dec(text, gamma))
                else:msgShow('Гамма не походит для шифруемого текста')

    def Freq_decrypt(self):
        text = self.ui.textEdit.toPlainText()
        if text == '': msgShow("Введите или загрузите текст для дешифровки")
        else:
            array_ch1 = AnalysisFreq.table_to_text(self.addWin.tableWidget,0)
            array_ch2 = AnalysisFreq.table_to_text(self.addWin.tableWidget,1)
            self.ui.textEdit_2.setText(AnalysisFreq.decrypt(text,array_ch1,array_ch2))


    def OpenAnalysisFreq(self):
        text = self.ui.textEdit.toPlainText()
        if text == '':msgShow("Введите или загрузите текст для дешифровки")
        else:
            self.addWin = AddWindowForFreq()
            self.addWin.show()
            AddWindowForFreq.AnalysisFr(self,text)
            self.addWin.pushButton_3.clicked.connect(self.Freq_decrypt)

    def MethIndTabl(self):
        min_ic = self.addWin.lineEdit.text()
        text = self.ui.textEdit.toPlainText()
        if min_ic == '':msgShow('Введите значение с которого будут учитываться индексы')
        else: AddWindowForPolyAlf.MethIC(self,text,min_ic)

    def PrintKeys1(self):
        AddWindowForPolyAlf.PrintKeysFor1(self)

    def PrintKeys2(self):
        AddWindowForPolyAlf.PrintKeysFor2(self)

    def MethAutoCorrel(self):
        text = self.ui.textEdit.toPlainText()
        AddWindowForPolyAlf.MethAutoCorrel(self,text)

    def MethKasiski(self):
        text = self.ui.textEdit.toPlainText()
        count_symb = self.addWin.lineEdit_2.text()
        if count_symb == '':msgShow('Введите количество символов, с которого нужно начать поиск повторов.')
        elif count_symb.isdigit(): AddWindowForPolyAlf.MethKasis(self,text,int(count_symb))
        else: msgShow('Введите число не больше 10 ')

    def VigDec(self):
        text = self.ui.textEdit.toPlainText()
        if text == '': msgShow('Ввежите текст для расшифровывания')
        else:
            key = self.ui.lineEdit.text()
            if key == '':msgShow('Введите ключ для расшифровывания')
            else: self.ui.textEdit_2.setText(Vigenere.dec(text,key))

    def OpenPolyAlfAnalysis(self):
        text = self.ui.textEdit.toPlainText()
        if text == '':msgShow("Введите или загрузите текст для дешифровки")
        else:
            self.addWin = AddWindowForPolyAlf()
            self.addWin.show()
            self.addWin.pushButton_2.clicked.connect(self.MethIndTabl)#рассчитать таблицу
            self.addWin.pushButton.clicked.connect(self.PrintKeys1)#расчитать варианты ключа
            self.addWin.pushButton_3.clicked.connect(self.MethKasiski)
            AddWindowForPolyAlf.PrintPlotAutoCorel(self, text)
            self.addWin.pushButton_4.clicked.connect(self.MethAutoCorrel)
            self.addWin.pushButton_5.clicked.connect(self.PrintKeys2)
            self.ui.pushButton_2.clicked.connect(self.VigDec)


app = QApplication([])
application = MainWin()
application.show()

def msgShow(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

sys.exit(app.exec())






