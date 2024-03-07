import numpy as np
from solucao import solucaoPressPress

po = 1900000
pw = 90000
phi = 0.2
mi = 0.5
k = 500
L = 100
ct = 10e-6
x = np.linspace(0, L, 1000)
t = np.linspace(0, 100, 10)

solucao = solucaoPressPress(po,pw,phi,mi,k,L,ct)
p= np.zeros((len(x),1))

p[:][0] = solucao.PressPress(x,t[5])