# import wavelets as wave
from wavelets import WAVE

def func(theta, x):                                                     #   ВХОД: ТЕТЫ, x - равный размер
    return sum(theta[i]*xi for i, xi in zip(range(len(theta)), x))

class MLE(object):
    def __init__(self, countMembers):
        self.N = countMembers

    def algFTLN(self, theta,X, Y, x, y, chm):
        m = len(Y)
        N = self.N[chm] #int(ip.membersOfRow.get())
        n = len(y)
        wave = WAVE(chm)
        ft = (1/n)**m
        for s in range(m):
            B = 0
            for j in range(n):
                for i in range(1, N+1, 1):
                    # t2 = 0.01
                    t1 = Y[s] - func(theta, X[s])
                    t2 = y[j] - func(theta, x[j])
                    B += wave.psi(t1, i)*wave.psi(t2, i)
            ft *= B
        return ft

    # solve(a*x+b,x) поиск решения x

    def algFTLNf(self, theta,X, Y, x, y, chm):
        m = len(Y)
        N = self.N[chm] #int(ip.membersOfRow.get())
        n = len(y)
        wave = WAVE(chm)
        ft = [0]*len(theta)
        for k in range(len(ft)):
            for s in range(m):
                B = 0
                A = 0
                for j in range(n):
                    for i in range(1, N+1, 1):
                        # t1 = 0.01
                        t1 = Y[s] - func(theta, X[s])
                        t2 = y[j] - func(theta, x[j])
                        psi1 = wave.psi(t1, i)
                        psi2 = wave.psi(t2, i)
                        B += psi1*psi2
                        A += wave.psiDef(X[s][k], t1, i)*psi1 + wave.psiDef(x[j][k], t2, i)*psi2
            ft[k] += A/B
        return ft   
