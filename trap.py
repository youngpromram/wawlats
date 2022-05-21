import math as mth
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.core.defchararray import count
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import median, trapz
import pandas as pd
from scipy.stats import expon
from scipy.stats import pearsonr
#from chigold import X2, gaussian, morlet, prib
import sympy
 
x = sympy.Symbol('x')

pi = mth.pi
mu=0
sigma=1

class wew(object):
       # N_point = 100; K_member = 5; n = N_point ; wawelet =0;z_min=0.5;z_max=1.5
    def __init__(self,N_point,K_member,x, xt,chm,k_s,j_s,bins) :
        self.N_point = N_point
        self.K_member = K_member
        self.x = x
        self.k_s=k_s
        self.j_s=j_s
        self.xt=xt
        self.chm=chm
        self.bins=bins
        

    def wawelet(self, t, i):
        if self.chm == 0:
            return self.morlet(t, i)
        elif self.chm == 1:
            return self.DOG(t, i)    
        elif self.chm == 2:
            return self.LP(t, i)
        elif self.chm == 3:
            return self.MH(t, i)


    def morlet(self, x, i):
        #считает лучше всего на средних сдначениях
         #   границы области
        c = min(self.x)
        d = max(self.x)
        kof=mth.sqrt(mth.sqrt(pi)/2)
        z=1/kof
         #   нормирование х
        x = (x) / (d - c)
        #   при i = 1 
        if i == 1:
            return  z * mth.sqrt(1 / (d - c))
        #   вычисляем чему равны k и j
        p = z * mth.sqrt(1 / (d - c)) * (2 ** ((self.k_s[i])/ 2)) * (mth.exp(-(((2 ** self.k_s[i]) * x - (self.j_s[i] - 1)) ** 2) / 2) * mth.cos(5 * ((2 ** self.k_s[i]) * x - (self.j_s[i]  - 1))))
        
        #p = z * mth.sqrt(1 / (d - c)) * (2 ** ((self.k[i])/ 2)) * (mth.exp(-(((2 ** self.k[i]) * x - (self.j[i] - 1)) ** 2) / 2) * mth.cos(5 * ((2 ** self.k[i]) * x - (self.j[i] - 1))))
        return p
   
    def DOG(self, x, i):
        #считает лучше всего на средних сдначениях
         #   границы области
        c = min(self.x)
        d = max(self.x)
        z=1.031/mth.sqrt(2)
         #   нормирование х
        x = (x-c) / (d - c)
        #   при i = 1 
        if i == 1:
            return z* mth.sqrt(1 / (d - c))
        p = z * mth.sqrt(1 / (d - c)) * (2 ** (self.k_s[i] / 2)) * ((mth.exp(-(((2 ** self.k_s[i]) * x - (self.j_s[i] - 1)) ** 2) / 2)) - 0.5 * (mth.exp(-(((2 ** self.k_s[i] ) * x - (self.j_s[i] - 1)) ** 2) / 8)))
        return p

    def DOG1(self, x, i):
        #считает лучше всего на средних сдначениях
         #   границы области
        c = min(self.x)
        d = max(self.x)
        #z=1.031/mth.sqrt(2)
         #   нормирование х
        x = (x-c) / (d - c)
        #   при i = 1 
        if i == 1:
            return z* mth.sqrt(1 / (d - c))
        #   вычисляем чему равны k и j
      

        k = int(mth.log2(i)) - 1
        j = i - 2 ** k

        p = z * mth.sqrt(1 / (d - c)) * (2 ** (k / 2)) * ((mth.exp(-(((2 ** k) * x - (j - 1)) ** 2) / 2)) - 0.5 * (mth.exp(-(((2 ** k ) * x - (j - 1)) ** 2) / 8)))
        return p

    def MH(self, x, i):
         #   границы области
        c = min(self.x)
        d = max(self.x)
         #   нормирование х
        z=1.031/mth.sqrt(2)
        x = (x-c) / (d - c)
        #   при i = 1 
        if i == 1:
            return z * mth.sqrt(1 / (d - c))
        #   вычисляем чему равны k и j
        k = int(mth.log2(i)) - 1
        j = i - 2 ** k
        kof=(2**(self.k_s[i]/2))*(1/mth.sqrt(d - c))

        #формула из статьи Елены Валерьевны
       # p = z * kof * (1-((2 ** self.k_s[i]) * x - (self.j_s[i] - 1))**2) * (mth.exp(-1/2*((2 ** self.k_s[i]) * x - (self.j_s[i] - 1))**2))
        # формула от Саши
        p = z * kof *(1 - 2*((2 ** self.k_s[i]) * x - (self.j_s[i] - 1))**2)*mth.exp(-((2 ** self.k_s[i]) * x - (self.j_s[i] - 1))**2)
        return p


    def LP(self, x, i):
        #считает лучше всего на средних сдначениях
         #   границы области
        c = min(self.x)
        d = max(self.x)
        
         #   нормирование х
        x = (x-c) / (d - c)
        #if (x==0.0000000):
         #   x=x+0.0000001
        if abs(x) < 1e-4: 
            x = 1e-4
        #   при i = 1 
        if i == 1:
            return mth.sqrt(1 / (d - c))
        h=mth.sqrt(1/(d-c))*(2**(self.k_s[i]/2))
        p = h* (mth.sin(2*pi*((2**self.k_s[i])*x - (self.j_s[i] - 1))) - mth.sin(pi*((2**self.k_s[i])*x - (self.j_s[i] - 1)))) / (pi*((2**self.k_s[i])*x - (self.j_s[i] - 1)))
        return p

    def LP1(self, x, i):
        # границы области
        c = min(self.x)
        d = max(self.x)
        
        if abs(x) < 1e-4: 
            x = 1e-6
        # нормирование х
        x = (x-c)/(d-c)
        # при i = 1
        if i == 1:
            return mth.sqrt(1/(d-c))
        # Вычисляем k и j
        k = self.k_s[i]
        j = i - 2**self.k_s[i]
        p = mth.sqrt(1/(d-c))*(2**(k/2)) * (mth.sin(2*pi*((2**k)*x - (j - 1))) - mth.sin(pi*((2**k)*x - (j - 1)))) / (pi*((2**k)*x - (j - 1)))
        return p

    def fp(self): 
        #if wawelet == 0:
        nt=len(self.xt) 
        for N in [self.K_member]:
            func = [0] * nt
            for t in range(nt):
                for i in range(1, N + 1):
                    F = sum(self.wawelet(self.x[j], i) * self.wawelet(self.xt[t], i) / self.N_point for j in range(self.N_point))
                    func[t] += F
                    np.savetxt('f.csv', func, delimiter=';')
        plt.plot(self.xt, func, label ='Вейвлет-оценка ')
        plt.hist(self.x, bins = self.bins, density = True)
        #np.histogram(self.x, bins = 10, density=True)
        #sns_plot = sns.distplot(self.x,bins = 10)
        #fig = sns_plot.get_figure()
        plt.legend()
        plt.show()
        return func
    
    