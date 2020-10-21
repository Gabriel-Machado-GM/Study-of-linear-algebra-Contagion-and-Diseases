# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:03:54 2020

@author: Gabriel Machado e Raphael Levy

Esse arquivo mostra o processo de desenvolvimento de um modelo
epidemiológico SIR, explica as várias variáveis e para fins de 
exemplificação há simulações no fim do arquivo.
"""

##############################################################################

# Importando as bibliotecas
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

##############################################################################

# N = População total.
N = 1000

##############################################################################

# I0, R0 = Número inicial de indivíduos infectados e recuperados respectivamente.
I0, R0 = 1, 0

##############################################################################

# S0 = Qualquer um é sucetível a infecção inicialmente, não há anticorpos. 
S0 = N - I0 - R0

##############################################################################

# Beta = Taxa de Contágio, Gama = média da recuperação de um indivíduo(1/dias).
beta, gamma = 0.2, 1./10 

##############################################################################

# Uma rede de espaço de tempo em dias.
t = np.linspace(0, 356, 365)

##############################################################################

# Equações diferenciais do modelo SIR. 
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

##############################################################################

# Condições iniciais do vetor.
y0 = S0, I0, R0

##############################################################################

# Integração do modelo de equações diferenciais do SIR na rede de tempo(t).
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

##############################################################################

# Coloque os dados em três curvas distintas para S(t), I(t) e R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (1000s)')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################
######################    SIMULAÇÕES     ####################################
##############################################################################

# Simulação número 1.

# População inicial fictícia.
N1 = 2000

# Números iniciais de infectados e recuperados.
I1, R1 = 500, 0

# Sucetíveis a contaminação.
S1 = N1 - I1 - R1

# Taxas técnicas.
beta1, gamma1 = 0.2, 1./10 

# Rede de tempo.
t1 = np.linspace(0, 60, 60)

# Equações diferenciais do modelo SIR.
def deriv(y1, t1, N1, beta1, gamma1):
    S1, I1, R1 = y1
    dSdt1 = -beta1 * S1 * I1 / N1
    dIdt1 = beta1 * S1 * I1 / N1 - gamma1 * I1
    dRdt1 = gamma1 * I1
    return dSdt1, dIdt1, dRdt1

# Condições inicias do vetor.
y1 = S1, I1, R1

# Integração do modelo de equações diferenciais do SIR na rede de tempo(t).
ret1 = odeint(deriv, y1, t1, args=(N1, beta1, gamma1))
S1, I1, R1 = ret1.T

# Plotando a simulação.
fig1 = plt.figure(facecolor='w')
ax = fig1.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t1, S1/1000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t1, I1/1000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t1, R1/1000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (1000s)')
ax.set_ylim(0,1.75)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulação número 2.

# População inicial fictícia.
N2 = 1000

# Números iniciais de infectados e recuperados.
I2, R2 = 200, 0

# Sucetíveis a contaminação.
S2 = N2 - I2 - R2

# Taxas técnicas.
beta2, gamma2 = 0.03, 2./10 

# Rede de tempo.
t2 = np.linspace(0, 50, 50)

# Equações diferenciais do modelo SIR.
def deriv(y2, t2, N2, beta2, gamma2):
    S2, I2, R2 = y2
    dSdt2 = -beta2 * S2 * I2 / N2
    dIdt2 = beta2 * S2 * I2 / N2 - gamma2 * I2
    dRdt2 = gamma2 * I2
    return dSdt2, dIdt2, dRdt2

# Condições inicias do vetor.
y2 = S2, I2, R2

# Integração do modelo de equações diferenciais do SIR na rede de tempo(t).
ret2 = odeint(deriv, y2, t2, args=(N2, beta2, gamma2))
S2, I2, R2 = ret2.T

# Plotando a simulação.
fig2 = plt.figure(facecolor='w')
ax = fig2.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t2, S2/1000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t2, I2/1000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t2, R2/1000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (1000s)')
ax.set_ylim(0,1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulação número 3, uma simulação básica do COVID no Brasil dia 21/10/2020.

# População no Brasil
N3 = 212205021 

# Números iniciais de infectados e recuperados.
I3, R3 = 5276942, 4721593 

# Sucetíveis a contaminação.
S3 = N3 - I3 - R3 

# Taxas técnicas.
beta3, gamma3 = 0.93, 1./10 

# Rede de tempo.
t3 = np.linspace(0, 60, 60) 

# Equações diferenciais do modelo SIR.
def deriv(y3, t3, N3, beta3, gamma3):
    S3, I3, R3 = y3
    dSdt3 = -beta3 * S3 * I3 / N3
    dIdt3 = beta3 * S3 * I3 / N3 - gamma3 * I3
    dRdt3 = gamma3 * I3
    return dSdt3, dIdt3, dRdt3

# Condições inicias do vetor.
y3 = S3, I3, R3

# Integração do modelo de equações diferenciais do SIR na rede de tempo(t).
ret3 = odeint(deriv, y3, t3, args=(N3, beta3, gamma3))
S3, I3, R3 = ret3.T

# Plotando a simulação.
fig3 = plt.figure(facecolor='w')
ax = fig3.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t3, S3/10000000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t3, I3/10000000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t3, R3/10000000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (10000000s)')
ax.set_ylim(0,25)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Bibliografia:
    #https://www.ibge.gov.br/apps/populacao/projecao/; 
    #https://www.gazetadopovo.com.br/republica/breves/taxa-de-recuperacao-da-covid-19-e-maior-no-brasil-que-espanha-italia-e-eua/;
    #https://g1.globo.com/bemestar/coronavirus/noticia/2020/10/13/taxa-de-transmissao-da-covid-19-fica-abaixo-de-1-pela-terceira-semana-seguida-no-brasil-aponta-imperial-college.ghtml
    
##############################################################################
