import MLE
import Main as M
import numpy as np
from tkinter import filedialog as fd

countV = 100
countT = 3

def readFile(fileName):
    data = []
    with open(fileName) as fin:                                                                                         #  
        for line in fin:
            data.append(float(line))
    return data

def culc(direct, drops, count):
    disp = []
    for bigNoise in [0.5]: #bigNoises:
        for drop in drops:
            for noise in [0.1, 0.3]: #noises:
                    for i in range(count):
                        FileName = direct + "/" + "e"+str(i) +" " + M.valuesDistribution[0] + " "+ " N=" + str(countV) + " T=" + str(countT) + " " + str(noise)+ " "+ str(drop)+" "+str(bigNoise)+".txt"
                        e = readFile(FileName)
                        disp.append(sum(ei for ei in e)/len(e))
    return disp

dir = fd.askdirectory()
res = culc(dir, [0.05, 0.1], 10)
fileres = "dispres"
np.savetxt(fileres, res)