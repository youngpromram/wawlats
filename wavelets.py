import math

class WAVE(object):
    def __init__(self, chm):
        self.chm = chm

    def psi(self, t, i):
        c = 0
        d = 10
        if i == 1: return self.startPoint(d-c)
        else:    
            if self.chm == 0:
                return self.MorleWave(t, i)
            elif self.chm == 1:
                return self.MHWave(t, i)    
            elif self.chm == 2:
                return self.DOGWave(t, i)
            elif self.chm == 3:
                return self.LPWave(t, i)
            elif self.chm == 4:
                return self.FurieWave(t, i)
    
    def psiDef(self, x, t, i):
        c = 0
        d = 10
        if i == 1: return 0
        else:    
            if self.chm == 0:
                return self.MorleWaveDef(x, t, i)
            elif self.chm == 1:
                return self.MHWaveDef(x, t, i)    
            elif self.chm == 2:
                return self.DOGWaveDef(x, t, i)
            elif self.chm == 3:
                return self.LPWaveDef(x, t, i)

    def startPoint(self, width):
        stp = math.sqrt(1/(width))
        if self.chm == 0:
            return stp*math.sqrt(2)/pow(math.pi, 1/4)/math.sqrt(1+math.exp(-25))
        elif self.chm ==1:
            return stp*1.031/math.sqrt(2)
        elif self.chm ==2:
            return stp*1.031/math.sqrt(2)
        elif self.chm ==3:
            return stp
        elif self.chm ==4:
            return stp

    def MHWave(self, t,i):
        c = 0
        d = 10
        z = 1.031/math.sqrt(2)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t-c)/(d-c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*(1 - 2*t**2)*math.exp(-t**2)
    
    def MHWaveDef(self, x, t,i):
        c = 0
        d = 10
        z = 1.031/math.sqrt(2)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t-c)/(d-c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*(2*t*x*math.exp(-1/2*t**2) + t*x*(1 - t**2)*math.exp(-1/2*t**2))

    def MorleWave(self, t, i):
        c = 0
        d = 10
        z = math.sqrt(2)/pow(math.pi, 1/4)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t - c)/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*math.exp(-t*t/2)*math.cos(5*t)
    
    def MorleWaveDef(self, x, t, i):
        c = 0
        d = 10
        z = math.sqrt(2)/pow(math.pi, 1/4)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t - c)/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*(t*x/2*math.exp(-t*t/2)*math.cos(5*t) + 5*x*math.exp(-t*t/2)*math.sin(5*t))

    def DOGWave(self, t, i):
        c = 0
        d = 10
        z = 1.031/math.sqrt(2)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t-c)/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*((math.exp(-t*t/2)) - math.exp(-t*t/8)/2)

    def DOGWaveDef(self, x, t, i):
        c = 0
        d = 10
        z = 1.031/math.sqrt(2)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t-c)/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*((t*x*math.exp(-t*t/2)) - 1/8*t*x*math.exp(-t*t/8))

    def LPWave(self, t, i):
        c = 0
        d = 10
        pi = math.pi
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t-c)/(d - c)
        t = pow(2,k)*t - (j-1)
        if abs(t) < 1e-4: 
            t = 1e-4
        return (2**(k/2))*math.sqrt(1/(d - c))*((math.sin(2*pi*t) - math.sin(pi*t))/(pi*t))

    def LPWaveDef(self, x, t, i):
        c = 0
        d = 10
        pi = math.pi
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = (t-c)/(d - c)
        t = pow(2,k)*t - (j-1)
        if abs(t) < 1e-4: 
            t = 1e-4
        return (2**(k/2))*math.sqrt(1/(d - c))*((-2*pi*x*math.cos(2*pi*t) + pi*x*math.cos(pi*t))*pi*t + pi*x*(math.sin(2*pi*t) - math.sin(pi*t)))/(pi*t)**2
    
    def FurieWave(self, t, i):
        c = 0
        d = 10
        pi = math.pi
        k = int(math.log(i-1, 2))
        j = i - 2**k
        # t = (t-c)/(d - c)
        # t = pow(2,k)*t - (j-1)
        
        if (i % 2) == 0:
            return math.sqrt(2/(d - c))*math.sin(pi*i/2*(t*2/(d - c) + (d + c)/(d - c)))
        else:
            return math.sqrt(2/(d - c))*math.cos(pi*(i - 1)/2*(t*2/(d - c) + (d + c)/(d - c)))
    