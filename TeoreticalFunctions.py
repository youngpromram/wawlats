import math as mth

# todo:
#       - убрать T, N и тд
#       
class TeoreticalFunctions(object):
    def __init__(self,
                parametrs,
                viewLimits):
        self.width = (viewLimits[1]-viewLimits[0])/2
        self.nPoint = 100
        self.expectation = parametrs[0]
        self.variance = parametrs[1]
        self.lambd = parametrs[2]
    
    def getFunction(self, chooseDistribution):
        if chooseDistribution == 0:
            return self.normalF()
        elif chooseDistribution == 1:
            return self.exponentialF()
        elif chooseDistribution == 2:
            return self.gammaF()

    def normalF(self):
        pi = mth.pi
        T = self.width
        N = self.nPoint
        m = self.expectation
        s = self.variance
        return [mth.exp(-((2*T*(i - N/2)/N)**2)/(2*s*s))/(s*mth.sqrt(2*pi)) for i in range(N+1)]
                

    def exponentialF(self):
        T = self.width
        N = self.nPoint
        return [self.lambd*mth.exp(-self.lambd*(2*T*(i)/N)) for i in range(N+1)]
    
    def gammaF(self):
        T = self.width
        N = self.nPoint
        m = self.expectation
        s = self.variance
        alf = m/s
        k = m*m/s
        return [((2*T*i/N)**(k-1))*mth.exp(-(2*T*i/N)*alf)*(alf**k)/mth.gamma(k) for i in range(N+1)]

    