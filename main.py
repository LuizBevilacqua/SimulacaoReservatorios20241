import numpy as np
from solucao import solucaoPressPress
import matplotlib.pyplot as plt

po  = 19000000
pw  = 9000000
qw  = 0.01
mi  = 0.001
k   = 9.869233e-14
h   = 10
phi = 0.2
ct  = 2.04e-9
L   = 10
A   = 30
x = np.linspace(1, L, 1000)
t = np.linspace(0, 100, 10)

solucao = solucaoPressPress(po,pw,phi,mi,k,L,ct)
p = np.zeros((len(t),len(x)))

for i in range(len(t)):
    p[i][:] = solucao.PressPress(x,t[i])

fig , ax = plt.subplots()
plt.ylabel('Press (psi)')
plt.xlabel('Comprimento (m)')
plt.title('PRESSÃO PRESSÃO - ANALÍTICO')

for i in range(len(t)):
    ax.plot(x,p[i][:], label='Press Press Analítica')

plt.show()