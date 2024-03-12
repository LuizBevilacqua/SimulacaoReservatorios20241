import numpy as np
from solucao import solucaoPressPress
from solucaoFluxo import solucaoFluxoPressao
import matplotlib.pyplot as plt

po  = 19000000
pw  = 9000000
qw  = 0.01
mi  = 0.001
k   = 9.869233e-14
h   = 10
phi = 0.2
ct  = 2.04e-9
L   = 20
A   = 30
x = np.linspace(0, L, 1000)
t = np.linspace(0, 100, 10)

solucaoPP = solucaoPressPress(po,pw,phi,mi,k,L,ct)
solucaoFP = solucaoFluxoPressao(po,qw,phi,mi,k,L,ct,A)
pPP = np.zeros((len(t),len(x)))
pFP = np.zeros((len(t),len(x)))

#imposto pressão inicial
#for i in range(len(x)):
#    pPP[0][i] = po

#for i in range(1,len(t)):
#    pPP[i][:] = solucaoPP.PressPress(x,t[i])

for i in range(len(t)):
    pPP[i][:] = solucaoPP.PressPress(x,t[i])
    pFP[i][:] = solucaoFP.fluxoPress(x,t[i])
fig , pressPress = plt.subplots()
plt.ylabel('Press (Pa)')
plt.xlabel('Comprimento (m)')
plt.title('PRESSÃO PRESSÃO - ANALÍTICO')

fig , fluxoPress = plt.subplots()
plt.ylabel('Press (Pa)')
plt.xlabel('Comprimento (m)')
plt.title('FLUXO PRESSÃO - ANALÍTICO')

for i in range(len(t)):
    pressPress.plot(x,pPP[i][:], label='Press Press Analítica')
    fluxoPress.plot(x,pFP[i][:], label='Fluxo Press Analítica')
plt.show()