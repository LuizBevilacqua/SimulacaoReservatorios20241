import numpy as np
import scipy as sp

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
        err = 100
        eppara = 10^-2
        n = 1
        sum = 0
        #while err>eppara:
         #   sum += np.exp(-(n*np.pi/self.L)**2*(self.k/(self.phi*self.mi*self.ct))*t)*np.sin(n*np.pi*x/self.L)
          #  n = n + 1
           # err = abs((sum-sumOld)/sum)*100
           # sumOld = sum 
        #p = (self.po - self.pw)*(x/self.L+2/np.pi*sum)+self.pw
        for j in range(1,10000):
            sum += (np.exp(-((j*np.pi/self.l)**2)*(self.k/(self.phi*self.mi*self.ct))*t)/j*np.sin(j*np.pi*x/self.l))
        p = (self.po - self.pw)*((x/self.l)+(2/np.pi)*sum)+self.pw
        return p
