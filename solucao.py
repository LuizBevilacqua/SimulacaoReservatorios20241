import numpy as np

class solucaoPressPress:
    def __init__(self,po,pw,phi,mi,k,L,ct):
        self.po = po
        self.pw = pw
        self.phi = phi
        self.mi = mi
        self.k = k
        self.l = L
        self.ct = ct

    def PressPress(self,x,t):
        p = np.zeros(len(x))
        sumOld = 100
        err = 1000
        eppara = 1e-3
        n = 0
        sum = 0
        while err >= eppara:
            n += 1
            i = n-1
            sum += (np.exp(-((n*np.pi/self.l)**2)*(self.k/(self.phi*self.mi*self.ct))*t)/n*np.sin(n*np.pi*x/self.l))
            err = abs((sum[i]-sumOld)/sum[i])*100
            sumOld = sum[i]
        p = (self.po - self.pw)*((x/self.l)+(2/np.pi)*sum)+self.pw
        return p
