import numpy as np
from scipy import optimize
import random as rnd
import math
import NonParametrEstmation as npe
from scipy.sparse.sputils import getdata
from RandomVariables import RandomVariables as RV
# from scipy.optimize.optimize import main
import MLE

сountMembers = [5,9,34,5, 9]
valuesFurie = [u"Дискретный", u"Быстрый", u"Прямоугольное окно", u"Окно Ханна", u"Окно Хемминга"]
valuesModel = [u"Морле", u"Мексиканская шляпа", u"DOG", u"LP", u"Фурье"]
valuesDistribution = [u"Нормальное распределение", u"Экспоненциальное распределение", u"Гамма-распределение", u"Бета-распределение"]

def fileData(fileName):                                                                                                 #   ВХОД: ИМЯ ФАЙЛА, ГДЕ ХРАНИТСЯ Y И X В СТРОКИ                                                                                                      #   
    with open(fileName) as fin:                                                                                         #  
        data = [np.array(line.split()).astype(np.float64) for line in fin]                                              #
        Y, X = np.split(data, [1])                                                                                      #
    return Y[0], X.T                                                                                                    #   ВЫХОД: МНОГОМЕРНЫЙ МАССИВ, ГДЕ [0] - У, ОСТАЛЬНОЕ X

def fileThets(fileName):
    file = open(fileName)                                                                                               #           ИМЯ ФАЙЛА С ТЕТТАМИ
    thets = [float(line) for line in file.readline().split()]                                                           #           ОБЪЕМ ВЫБОРКИ
    file.close()
    return thets


def withNoise(Y, noise, drop, chd, bigNoise):                                                                                     #   ВХОД: ТОЧНЫЙ Y, ДЛЯ ШУМА, ДЛЯ ВЫБРОСОВ
    n = len(Y)                                                                                                          #   
    dy = sum(yi for yi in Y)/n                                                                                          #   Добавляет шум в выборку
    w = sum((yi-dy)**2 for yi in Y)/(n-1)                                                                               #
    y = [yi for yi in Y]                                                                                                #
                                                                                                                        #
    # bigNoise = 2                                                                                                        #
    
    parametrs = [0,1,0.5, 1, 9,2]                                                                                       #
    randomVariables = RV(len(y), parametrs)                                                                             #
    rv = randomVariables.getFunction(chd) 
    
    for i, rvi in zip(range(len(y)), rv):                                                                               #
        requency = rnd.uniform(0,1)                                                                                     #
        if(drop == '' or requency >= drop):                                                                             #
            y[i] += rvi*noise*math.sqrt(w)                                                                             #
        else:                                                                                                           #
            y[i] += rvi*bigNoise*math.sqrt(w)                                                                           #
    return y                                                                                                            #   ВЫХОД: у с шумом

def createData(direct, fileName, countV, noise, drop,chd, bigNoise, i):                                                                       #   ВХОД:   ДИРРЕКТОРИЯ ДЛЯ ДАННЫХ
    thets = fileThets(fileName)                                                                                                        #           КОЛЛИЧЕСТВО ТЕТ
    # thets = [thets[i] for i in range(countT)]                                                                           #
    countT = len(thets)
    X = []
    x = [rnd.uniform(-1,1) for j in range(countV)]
    for j in range(countT):
        X.append([xi**j for xi in x])
    X=np.array(X).T
    # X = np.array([[rnd.uniform(-1,1) for i in range(countV)] for j in range(countT)]).T                         #    !!!!!поменять
    Y = Y1 = [MLE.func(thets, xi) for xi in X]                                                                               #
    Y = withNoise(Y, noise, drop,chd, bigNoise)
    e = np.array([yi - y1 for yi, y1 in zip(Y, Y1)])
    data = np.vstack([np.array(Y), X.T])                                                                                #   ЗАПИСЬ В ФАЙЛ
    resFileName = direct + "/" + "data"+str(i) +" " + valuesDistribution[chd] + " "+ " N=" + str(countV) + " T=" + str(countT) + " noise=" + str(noise)+ " drop="+ str(drop)+" BigNoise="+str(bigNoise)+".txt"                            #
    np.savetxt(resFileName, data)                                                                                       #
    eFileName = direct + "/" + "e"+str(i)+" "+ valuesDistribution[chd] + " "+ " N=" + str(countV) + " T=" + str(countT) + " " + str(noise)+ " "+ str(drop)+" "+str(bigNoise)+".txt"
    np.savetxt(eFileName, e.T)
    return fileData(resFileName)                                                                                        #   ПОЛУЧЕНИЕ ДАННЫХ ИЗ ФАЙЛА
    
def culcNu(Y, X, thets):
    #для файла                                                                                                #   ВХОД: ТОЧНЫЕ Y X, ПОЛУЧЕНЫЕ thets
    n = len(Y)                                                                                                          #
    y = [MLE.func(thets, xi) for xi in X]                                                                               #
    return math.sqrt(sum((y1-y2)**2 for y1, y2 in zip(Y, y)))/(n-1)                                                     #   ВЫХОД: дисперсия между точным y и полученым

def printRes(fileName, resT, resNu):                                                                                    #   ВХОД: ИМЯ ИТОГОВОГО ФАЙЛА, МАСИВ ТЕТ, МАСИВ МЮ
    file = open(fileName, "w", encoding="utf-8")                                                                        #
    for model, t, nu in zip(valuesModel, resT, resNu):                                                                  #
        file.write("Received for {}: {}\n".format(model,t))                                                             #
        file.write("nu = {0:.4f}\n\n".format(nu))                                                                       #
    file.close()                                                                                                        #    

def getSP(X, Y):
    m = X.T @ X                                                     # МАТРИЦА ВЫРОЖДЕНАЯ 
    # while np.linalg.det(m) == 0:                                    # хз что делать
    #     m,x = np.array(np.split(m.T, [len(m.T)-1]))
    #     m,x = np.array(np.split(m.T, [len(m.T)-1]))
        # X,x = np.array(np.split(X.T, [len(X.T)-1]))
        # X=X.T
    thets = np.linalg.inv(X.T @ X) @ X.T @ Y
    return thets

def getXY(X, Y):
    size = 32
    I = [int(i/size * (len(Y)-1)) for i in range(size)]
    x = np.array([X[i] for i in I])
    y = np.array([Y[i] for i in I])
    return x,y

def mainFromFile(direct, file, countMembers):
    Y, X = fileData(file)
    thets = [] 
    nus = []
    mle = MLE.MLE(countMembers)
    for chm in range(len(valuesModel)):                                                                                                        # добавить шум y
        x,y = getXY(X,Y)
                                                                                                                # начать цикл по параметру сглаживания
                                                                                                                # по мнк найти начальную точку
        startT = getSP(x, y)
                                                                                                                # optimize
        res = optimize.minimize(mle.algFTLN, startT, args=(x,y,X,Y,chm), method='SLSQP')#, jac = mle.algFTLNf) 
                                                                                                                # nu
        mas = res.x

        thets.append(mas)
        nus.append(culcNu(Y, X, thets[chm]))
                                                                                                                # вывести данные
    fileName = direct + "/из файла.txt"
    thets.append(startT)
    nus.append(culcNu(Y,X,thets[chm+1]))
    valuesModel.append("МНК")
    printRes(fileName, thets, nus)
    valuesModel.pop()

def mainWithGen(direct, file, bigNoises, drops, chd, noises, countV, countS, countM):
    
    # if WITHD:
    #     bigNoises = [0.5, 1, 2]
    # else:
    #     bigNoises = ['']
    mle = MLE.MLE(countM)
    for bigNoise in bigNoises:
        for drop in drops:
            for noise in noises:
                thets = []
                nus = []
                sts = []
                for chm in range(len(valuesModel)):
                    athets = []
                    count = countS
                    for i in range(count):
                        Y, X = createData(direct, file,  countV, noise, drop,chd, bigNoise, i)
                        # Y = withNoise(Yt, noise, drop,chd, bigNoise)
                        x,y = getXY(X, Y)
                        startT = getSP(x, y)
                        res = optimize.minimize(mle.algFTLN, startT, args=(x,y,X,Y,chm), method='SLSQP')#, jac = mle.algFTLNf)
                        resT = res.x
                        athets.append(resT)
                        sts.append(startT)
                    mas = []
                    for i in range(len(athets[0])):
                        mas.append(sum(at[i] for at in athets)/count)
                    thets.append(mas)
                    nus.append(culcNu(Y, X, thets[chm])) 
                fileName = direct + "/" + valuesDistribution[chd] + " " + str(noise)+ " "+ str(drop)+" "+str(bigNoise) + ".txt"
                ST = []
                for i in range(len(sts[0])):
                    ST.append(sum(s[i] for s in sts)/len(sts))
                thets.append(ST)
                nus.append(culcNu(Y, X, thets[chm+1]))
                valuesModel.append("МНК")
                printRes(fileName, thets, nus)
                valuesModel.pop()

def mainEst(fileD, fileP, kMember, choosModel, chooseDistribution):
    Y, X = fileData(fileD)
    thets = fileThets(fileP)
    viewLimits = npe.getViewLimits(chooseDistribution)
    randomVariables = [y - MLE.func(thets, x) for y,x in zip(Y,X)]
    fourierTransform = npe.FourierTransform(randomVariables,
                                            len(randomVariables),
                                            kMember,
                                            viewLimits)
    evalution = fourierTransform.getEstmation(choosModel)
    npe.showDensityFunction(evalution, chooseDistribution)
    result = npe.outputOfResults(evalution, chooseDistribution)
    return result


# mainEst('data1 N=100 T=3 noise=0.05.txt', 'thets.txt', 0)



