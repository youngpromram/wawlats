
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from scipy.sparse.sputils import getdata
import RegressMain as M
from NonParametrEstmation import creater

def sendErrMes(text):
    mb.showerror(
            "Message", 
            text)
def sendInfMes(text):
    mb.showinfo(
            "Message", 
            text)
class Estf(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.valuesDistribution = parent.valuesDistribution
        self.valuesModel = parent.valuesFurie
        self.filesName = [0]*2
        self.isData = [False]*2
        self.frame1()
        # self.frame2()
        self.frame3()

    def frame1(self):
        frame = LabelFrame(self)
        frame.grid(column=0, row=0)
        Label(frame, text = "Фурье: "               ).grid(column=0, row=0,pady = (0, 0), padx=(30, 0))
        Label(frame, text="Количество членов ряда:" ).grid(column=0, row=2,pady = (0, 0), padx=(30, 0))
        Label(frame, text = "Функция распределения:").grid(column=0, row=3,pady = (0, 0), padx=(30, 0))
        Label(frame, text="Файл с данными"          ).grid(column=0, row=4,pady = (0, 0), padx=(30, 0))
        Label(frame, text="Файл с параметрами"      ).grid(column=0, row=5,pady = (0, 0), padx=(30, 0))

        self.chooseModel = Combobox(frame, values=self.valuesModel)
        self.chooseModel.set(self.valuesModel[0])

        self.membersOfRow = StringVar()
        self.membersOfRow.set('10')
        frameMembersOfRow = Entry(frame, width=23, textvariable = self.membersOfRow)

        self.chooseDistribution = Combobox(frame, values = self.valuesDistribution)
        self.chooseDistribution.set(self.valuesDistribution[0])

        butData = Button(frame, text="Выбрать", command=lambda:self.getFileName(0))
        butThets = Button(frame, text="Выбрать", command=lambda:self.getFileName(1))
        
        self.chooseModel.grid(          column=1, row=0, pady=(10, 0), padx=(5, 0))
        frameMembersOfRow.grid(         column=1, row=2, pady=(10, 0), padx=(5, 0))
        self.chooseDistribution.grid(   column=1, row=3, pady=(10, 0), padx=(5, 0))
        butData.grid(column=1, row=4, padx=(40, 40), pady=(10, 0))
        butThets.grid(column=1, row=5,padx=(40, 40), pady=(10, 0))

    def frame2(self):
        frame = LabelFrame(self, text="Для ОПФ")
        frame.grid(column=0, row=1)

        Label(frame, text="Введите количество окон:").grid(column=0, row=0, pady = (0, 0), padx=(30, 0))
        Label(frame, text="Введите размер окон:"    ).grid(column=0, row=1, pady = (0, 0), padx=(30, 0))

        self.numOfWindow = StringVar()
        self.numOfWindow.set(0)
        frameNumOfWindow = Entry(frame, width=23, textvariable = self.numOfWindow)

        self.widthOfWindow = StringVar()
        self.widthOfWindow.set(0)
        frameWidthOfWindow = Entry(frame, width=23, textvariable = self.widthOfWindow)

        frameNumOfWindow.grid(  column=1, row=0, pady=(10, 0), padx=(5, 0))
        frameWidthOfWindow.grid(column=1, row=1, pady=(10, 0), padx=(5, 0))


    def frame3(self):
        frame = LabelFrame(self)
        frame.grid(column=1, row=0, rowspan=2)

        self.output = Text(frame, bg="white", font="Arial 10", width = 50, height = 12)
        
        butSimple = Button(  frame, text="Решить", command=lambda:self.creater())

        self.output.grid(    column=0, row=0, columnspan=4)
        butSimple.grid(      column=0, row=1, padx=(40, 0), pady=(10, 0))
    def insertval(self, value):
        self.output.insert("1.0", value)
    def creater(self):
        text = "обычный 1 раз\n"
        if self.isData[0] and self.isData[1]:
            fileD = self.filesName[0]
            fileP = self.filesName[1]
        else:
            sendErrMes("Не выбраны файлы с данными")
        kMember = int(self.membersOfRow.get())
        chooseDistribution = self.chooseDistribution.current()
        chooseModel = self.chooseModel.current()
        text = M.mainEst(fileD, fileP, kMember, chooseModel, chooseDistribution)
        self.insertval(text)
    
    def getFileName(self, i):
        self.filesName[i] = fd.askopenfilename()
        if self.filesName[i]:
            self.isData[i] = True
            # self.WithThets = WithThets
            # self.dataFC = False
        else:
            sendErrMes("Не выбран файл")
        

class About(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.endT = False
        self.chf = False
        self.valuesDistribution = parent.valuesDistribution
        self.createFrame2()
        
    def createFrame2(self):
        frame = LabelFrame(self)
        frame.grid(column=0, row=0)

        Label(frame, text="Выбросы"                       ).grid(column=0, row=0)
        Label(frame, text="Область выбросов до 50%: "     ).grid(column=0, row=1)
        Label(frame, text="Функция распределения: "       ).grid(column=0, row=2)
        Label(frame, text="Шум до 50% с шагом: "          ).grid(column=0, row=3)
        Label(frame, text="Объем генерируемой выборки: "  ).grid(column=0, row=4)
        Label(frame, text="Количество выборок: "          ).grid(column=0, row=5)
        Label(frame, text="Файл с параметрами: "          ).grid(column=0, row=6)

        self.withDrop = IntVar()
        checkDrop = Checkbutton(frame, text="", variable=self.withDrop)
       
        self.stepMu = StringVar()
        self.stepMu.set(5)
        framestepMu = Entry(frame, textvariable=self.stepMu)

        
        self.chooseDistribution = Combobox(frame, values = self.valuesDistribution)
        self.chooseDistribution.set(self.valuesDistribution[0])

        self.stepErr = StringVar()
        self.stepErr.set(5)
        framestepErr = Entry(frame, textvariable=self.stepErr)

        self.countV = StringVar()
        self.countV.set(100)
        frameCountV = Entry(frame, textvariable=self.countV)

        self.countS = StringVar()
        self.countS.set(10)
        frameCountS = Entry(frame, textvariable=self.countS)
        
        buttoChooseFile = Button(frame, text="Выбрать", command=lambda : self.getFileName())
        

        buttoEnd = Button(frame, text="Готово", command=lambda : self.close())
        
        checkDrop.grid(         column=1, row=0, pady=(5, 5), padx=(5, 5))
        framestepMu.grid(       column=1, row=1, pady=(5, 5), padx=(5, 5))
        self.chooseDistribution.grid(column=1, row=2, pady=(5, 5), padx=(5, 5))
        framestepErr.grid(      column=1, row=3, pady=(5, 5), padx=(5, 5))
        frameCountV.grid(       column=1, row=4,pady=(5, 5), padx=(5, 5))
        frameCountS.grid(       column=1, row=5, pady=(5, 5), padx=(5, 5))
        buttoChooseFile.grid(   column=1, row=6, pady=(5, 5), padx=(5, 5))
        buttoEnd.grid(          column=1, row=7, pady=(5, 5), padx=(5, 5))
    
    def close(self):
        self.endT = True
        self.chd = self.chooseDistribution.current()
        self.destroy()

    def getFileName(self):
        self.fileName = fd.askopenfilename()
        if self.fileName:
            self.chf = True
        else:
            sendErrMes("Не выбран файл")

    def getData(self):
        self.grab_set()
        self.wait_window()
        
        return self


class App(Tk):
    def __init__(self, valuesModel,valuesDistribution, valuesFurie, сountMembers):
        super().__init__()
        
        self.valuesModel = valuesModel
        self.valuesDistribution = valuesDistribution
        self.valuesFurie = valuesFurie
        self.сountMembers = сountMembers

        self.isData = False
        self.dataFC = False

        self.createFrame1()
        self.createFrame2()
        self.createFrame3()

    # def sendErrMes(text):
    #     mb.showerror(
    #             "Message", 
    #             text)
    # def sendInfMes(text):
    #     mb.showinfo(
    #             "Message", 
    #             text)

    def createFrame1(self):
        # frame = LabelFrame(self)
        # frame.grid(column=0, row=1)

        self.buttonGenerate = Button(self, text="Сгенерировать", command=lambda : self.open_window())
        self.buttonGenerate.grid(column=0, row=0)

        self.buttoChooseFile = Button(self, text="Выбрать из файла", command=lambda : self.getFileName())
        self.buttoChooseFile.grid(column=1, row=0)

    def createFrame2(self):
        frame = LabelFrame(self)
        frame.grid(column=0, row=2, columnspan=2)
        # self.CountMembers = [5,8,8,5]
        self.textCountMembers =[StringVar()]*len(self.сountMembers)
        for i in range(len(self.сountMembers)):
            a = StringVar()
            a.set(self.сountMembers[i])
            self.textCountMembers[i] = a
        
        for i in range(len(self.valuesModel)):
            Label(frame, text="Параметры сглаживания {}:".format(self.valuesModel[i])).grid(column=0, row=i, pady = (5, 5), padx=(30, 0))
            Entry(frame, textvariable=self.textCountMembers[i]).grid(column=1, row=i, pady=(5, 5), padx=(5, 5))

    def createFrame3(self):
        # frame = LabelFrame(self)
        # frame.grid(column=0, row=3)
        # buttonEst = Button(self, text="ОФП", command=lambda:self.open_est())
        # buttonEst.grid(column=0, row=3, padx=(40,40), pady=(10,0))
        buttonStart = Button(self, text="Решить", command=lambda : self.callMain())
        buttonStart.grid(column=1, row=3, padx=(40, 40), pady=(10, 0))

    def open_est(self):
        est = Estf(self)
        
    def open_window(self):
        # self.isData = True
        about = About(self)
        self.dataFC = about.getData()
        self.isData = self.dataFC.endT
        if not self.isData:
            sendErrMes("Не выбраны данные")

    def getFileName(self):
        self.fileName = fd.askopenfilename()
        if self.fileName:
            self.isData = True
            # self.WithThets = WithThets
            self.dataFC = False
        else:
            sendErrMes("Не выбран файл")    
    
    
    
    def callMain(self):
        if not self.isData:
            sendErrMes("Не выбраны данные")
            return 0
        
        direct = fd.askdirectory()
        if not direct:
            sendErrMes("Не выбрана дирректория")
            return 0
        if self.dataFC and self.dataFC.endT:
            print("генерация")
            if not self.dataFC.chf:
                sendErrMes("Не выбран файл с параметрами для генерации")
                return 0
            file = self.dataFC.fileName
            Drops = self.getDrops(self.dataFC.withDrop.get(), self.dataFC.stepMu.get())
            bigNoises = self.getBN(Drops)
            ChooseDistribution = self.dataFC.chd
            Noises = self.getNoises(self.dataFC.stepErr.get())
            CountV = int(self.dataFC.countV.get())
            CountS = int(self.dataFC.countS.get())
            countMembers = self.сountMembers
            M.mainWithGen(direct, file, bigNoises, Drops, ChooseDistribution, Noises, CountV, CountS, countMembers)
            self.isData = False
            
        else:
            print("файл")
            file = self.fileName
            countMembers = self.сountMembers
            M.mainFromFile(direct, file, countMembers)
            self.isData = False
            
        sendInfMes("Закончили")
        # M.Main(self.forGen, WithThets, ChooseDis, Drops, Noises, CountMembers, countM)

    def getBN(self, mas):
        if mas[0]=='':
            return ['']
        else:
            return [0.5, 1, 2]

    def getDrops(self, withDrop, stepMu):
            if withDrop == 0:
                return ['']
            else: 
                stepMu = int(stepMu)
                return [i/100 for i in range(stepMu, 51, stepMu)]
    
    def getNoises(self, stepErr):
        stepErr = int(stepErr)
        return [i/100 for i in range(stepErr, 51, stepErr)]

if __name__ == "__main__":
    app = App(M.valuesModel, M.valuesDistribution, M.valuesFurie, M.сountMembers)
    app.mainloop()