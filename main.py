################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

from msilib.schema import Directory
import sys
import platform
import re
import random as rnd
import numpy as np 

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import os
from subprocess import call
# GUI FILE
from app_modules import *

import MainS as M
from RandomVariables  import RandomVariables
import NonParametrEstmation as npe
#from newgold import gold

from xtclass import xt_pandas
#from trap import gold
from trap import wew

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('WTiRM V1.0')
        UIFunctions.labelTitle(self, 'WTiRM V1.0')
        UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Главная страница", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Вейвлеты", "btn_new_user", "url(:/16x16/icons/16x16/cil-options-horizontal.png)", True)
        UIFunctions.addNewMenu(self, "Фурье", "btn_new_fur", "url(:/16x16/icons/16x16/cil-options-horizontal.png)", True)
        UIFunctions.addNewMenu(self, "Регрессия", "btn_new_reg", "url(:/16x16/icons/16x16/cil-options-horizontal.png)", True)
        
         ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##
        self.ui.pushButton.pressed.connect(self.wewlet)
        self.ui.pushButton_3.pressed.connect(self.fur)
        #self.ui.buttonStart.pressed.connect(self.open_file)
        self.ui.buttonStart.pressed.connect(self.reg)
        self.ui.filebutton_parametrs.clicked.connect(self.getFileName)
        self.ui.filebutton.clicked.connect(self.showDialog)
        ## USER ICON ==> SHOW HIDE
        if self.ui.checkBox.isChecked()==1:
            self.ui.comboBox_2.activateWindow        #
        # self.ui.checkBox.activateWindow(1)
        ## ==> END ##
       

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "ГЛАВНАЯ СТРАНИЦА")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "ОЦЕНИВАНИЕ ФУНКЦИИ ПЛОТНОСТИ НА ОСНОВЕ ВЕЙЛЕТ АНАЛИЗА")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
               

        if btnWidget.objectName() == "btn_new_fur":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
            UIFunctions.labelPage(self, "ОЦЕНИВАНИЕ ФУНКЦИИ ПЛОТНОСТИ НА ОСНОВЕ ПРЕОБРАЗОВАНИЙ ФУРЬЕ")
            UIFunctions.resetStyle(self, "btn_new_w")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        if btnWidget.objectName() == "btn_new_reg":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
            UIFunctions.labelPage(self, "АДАПТИВНОЕ ОЦЕНИВАНИЕ ПАРАМЕТРОВ РЕГРЕССИИ")
            UIFunctions.resetStyle(self, "btn_new_f")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##
    
    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    def fur(self):
        text = self.ui.lineEdit_15.text()
        membersOfRow=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        text = self.ui.lineEdit_5.text()
        sampleSize=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        chooseDistribution=self.ui.comboBox_choiceD.currentIndex()
        chooseModel= self.ui.comboBox_choiceModel.currentIndex()
        res = npe.creater(sampleSize, membersOfRow, chooseDistribution, chooseModel)
        return res

    def wewlet(self):
        text = self.ui.lineEdit.text()
        print(text)
        membersOfRow=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        text = self.ui.lineEdit_4.text()
        sampleSize=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        print(sampleSize)
        chooseDistribution=self.ui.comboBox_2.currentIndex()
        
        chm=self.ui.comboBox.currentIndex()
        print(chm)
    
        if self.ui.checkBox.isChecked()==True:
            text = self.ui.lineEdit_path.text()
            data=open(text).read().split('\n')

            print(data)
            float_list=[float(x) for x in data]
            x=sorted(float_list)
            print(x)
            sampleSize=len(x)
        else:
            x=npe.getRandomVariables(sampleSize,chooseDistribution)
            x = sorted(x)
            np.savetxt('v_teor.csv', x, delimiter=';')
        per=xt_pandas(x)
        xt=per.Xa()
        bins=per.bins()
        
        k, j = per.k_j_i()
        wewl=wew(sampleSize,membersOfRow,x, xt,chm,k,j,bins)
    # ipe.insertval(outputOfResults(evalution))
        #print(wewl.simpson_rule(bins))
        return wewl.fp()
        #golddnew = gold(sampleSize,membersOfRow,x, xt,chm,k,j)
        #return golddnew.Golden_Section_Method(0.5,1.5,0.01)
        #tr=gold(sampleSize,membersOfRow,x, xt,chm,k,j)
        #return tr.tpapezia(1)

   

    def getDirectory(self):                                                     # <-----
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        return (dirlist)
        
    def reg(self):
        countMembers=[]
        text = self.ui.lineEdit_morle.text()
        member_Morle=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        countMembers.append(member_Morle)

        text = self.ui.lineEdit_MH.text()
        member_MH=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        countMembers.append(member_MH)

        text = self.ui.lineEdit_Dog.text()
        member_Dog=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        countMembers.append(member_Dog)

        text = self.ui.lineEdit_LP.text()
        member_LP=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        countMembers.append(member_LP)

        text = self.ui.lineEdit_f.text()
        member_f=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        countMembers.append(member_f)

        text = self.ui.lineEdit_step.text()
        stepErr=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
         
        text = self.ui.lineEdit_v.text()
        stepMu=int("0"+"".join(list(map(str, re.findall(r'\d+', text))))) 

        print(countMembers) 
        withDrop=self.ui.checkBox_witDrops.isChecked()
        #необходимо подключить сигнал от радиобатона
        Drops = self.getDrops(withDrop,stepMu)
        #Drops = stepMu
        bigNoises = self.getBN(Drops)
        ChooseDistribution=self.ui.comboBox_choiceD_2.currentIndex()
      
        Noises = self.getNoises(stepErr)

        text = self.ui.lineEdit_kilvo.text()
        CountS=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))

        text = self.ui.lineEdit_vv.text()
        CountV=int("0"+"".join(list(map(str, re.findall(r'\d+', text)))))
        file = self.ui.lineEdit_path.text()
        print(file)
        #file=open(text).read().split('\n')
        direct=self.getDirectory()
        file=self.getFileName()
        self.ui.lineEdit_pathpar.setAccessibleName(file)
        print(direct)
        print(file)
        M.mainWithGen(direct, file, bigNoises, Drops, ChooseDistribution, Noises, CountV, CountS, countMembers)

    def getBN(self, mas):
        if mas[0]=='':
            return ['']
        else:
            return [0.5, 1, 2]

    def getDrops(self, withDrop, stepMu):
            if withDrop == False:
                return ['']
            else: 
                stepMu = int(stepMu)
                return [i/100 for i in range(stepMu, 51, stepMu)]
    
    def getNoises(self, stepErr):
        stepErr = int(stepErr)
        return [i/100 for i in range(stepErr, 51, stepErr)]    
        

    def open_file(self):
        os.system('interface.exe')
        #call(['python', 'interface.py'])
    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################
    def showDialog1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.ui.lineEdit_pathpar.setAccessibleName(fname)
        #self.ui.label_path.setText(fname)
        self.ui.lineEdit_pathpar.setText(fname)
        return fname
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.ui.lineEdit_path.setAccessibleName(fname)
        #self.ui.label_path.setText(fname)
        self.ui.lineEdit_path.setText(fname)
        #print(fname)
        #print("write")
        return fname
    
    def getFileName(self):
        filename = QFileDialog.getOpenFileName(self, "Выбрать файл")[0]
        return (filename)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows Style')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
