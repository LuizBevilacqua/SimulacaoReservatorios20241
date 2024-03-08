import numpy as np
from scipy import special

class solucaoFluxoPressao:
    def __init__(self,po,qw,phi,mi,k,L,ct,A):
        self.po = po
        self.qw = qw
        self.phi = phi
        self.mi = mi
        self.k = k
        self.l = L
        self.ct = ct
        self.a = A

    def fluxoPress(self,x,t):
        p = np.zeros(len(x))
        eta = self.k/(self.phi*self.mi*self.ct)
        p = self.po - self.qw*self.mi*self.l/(self.k*self.a)*(np.sqrt(4*eta*t/(np.pi*self.l**2))*np.exp(-x**2/(4*eta*t))-x/self.l*special.erfc(x/np.sqrt(4*eta*t)))
        return p
