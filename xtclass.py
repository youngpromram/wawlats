import math as mth
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import count
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import median
import pandas as pd
from scipy.stats import expon
from scipy.stats import pearsonr

#from chigold import X2, gaussian, morlet, prib

#from chigold import X2, gaussian, morlet, prib


pi = mth.pi
mu=0
sigma=1

class xt_pandas(object):
       # N_point = 100; K_member = 5; n = N_point ; wawelet =0;z_min=0.5;z_max=1.5
    def __init__(self,x) :
        self.x = x

    def Xa(self):
        N = len(self.x)
    #формула стердженса
        k = 99
        print(k)
    #делем на сколько было
        h = (max(self.x)-min(self.x))/k
        print(h)
        #bins=[]
        d=[]
    #print(F_teor)
        for i in range(k+1):
            d.append(min(self.x)+h*i)
            #bins.append(min(self.x)+h*i)
        #s=pd.Series(self.x)
        #d=s.groupby(pd.cut(self.x,bins,include_lowest=True)).apply(lambda x: mean(x.to_list()))

    #print(d)
    #print(dd)
    
        d[0]=min(self.x)
        d[k-1]= max(self.x)
        #d[0]=min(self.x)
        #d[k-1]= max(self.x)
        print(d)
        return  d
    def bins(self):
        N = len(self.x)
        #формула стердженса
        k = round(1 + mth.log2(N))
        return(k)
    def k_j_i(self):
        k=[]
        j=[]
        
        for u in range(7):
            for f in range(2**u):
                k.append(u)
                j.append(f+1)
        print(k)
        print(j)
        k=pd.Series(k)
        j=pd.Series(j)
        k.index+=2
        j.index+=2
        print(k)
        print(j)
        return (k,j)

    def Xa2(self):
        N = len(self.x)
        #формула стердженса
        k = round(1 + mth.log2(N))
        #k=15
        #print(k)
        #делем на сколько было
        #h = ((max(self.x)-0.5)-(min(self.x)+0.5))/k
        #print(h)
        h = (max(self.x)-min(self.x))/k
        bins=[]
        #print(F_teor)
        for i in range(k+1):
            bins.append(min(self.x)+h*i)
            #bins.append((min(self.x)-0.5)+h*i)
        
        #print(bins)
        s=pd.Series(self.x)
        x=self.x
        d=s.groupby(pd.cut(x,bins,include_lowest=True)).apply(lambda x: median(x.to_list()))
        return d