##############################################################################

# Importando as bibliotecas
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

##############################################################################

# N = Populacao total.
N = 1000

##############################################################################

# I0, R0 = Numero inicial de individuos infectados e recuperados respectivamente.
I0, R0 = 1, 0

##############################################################################

# S0 = Qualquer um e suscetivel a infeccao inicialmente, nao ha anticorpos. 
S0 = N - I0 - R0

##############################################################################

# Beta = Taxa de Contagio, Gama = media da recuperacao de um individuo(1/dias).
beta, gamma = 0.2, 1./10 

##############################################################################

# Uma rede de espaco de tempo em dias.
t = np.linspace(0, 150, 150)

##############################################################################

# Equacoes diferenciais do modelo SIR. 
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

##############################################################################

# Condicoes iniciais do vetor.
y0 = S0, I0, R0

##############################################################################

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

##############################################################################

# Coloque os dados em tres curvas distintas para S(t), I(t) e R(t)
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
######################    SIMULACOES     ####################################
##############################################################################

# Simulacao numero 1, uma simulacao basica do COVID no Brasil dia 21/10/2020.

# Populacao no Brasil
N1 = 212205021 

# Numeros iniciais de infectados e recuperados.
I1, R1 = 5276942, 4721593 

# Suscetiveis a contaminacao.
S1 = N1 - I1 - R1 

# Taxas tecnicas.
beta1, gamma1 = 0.93, 0.8/10 

# Rede de tempo.
t1 = np.linspace(0, 100, 100) 

# Equacoes diferenciais do modelo SIR.
def deriv(y1, t1, N1, beta1, gamma1):
    S1, I1, R1 = y1
    dSdt1 = -beta1 * S1 * I1 / N1
    dIdt1 = beta1 * S1 * I1 / N1 - gamma1 * I1
    dRdt1 = gamma1 * I1
    return dSdt1, dIdt1, dRdt1

# Condicoes inicias do vetor.
y1 = S1, I1, R1

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret1 = odeint(deriv, y1, t1, args=(N1, beta1, gamma1))
S1, I1, R1 = ret1.T

# Plotando a simulacao.
fig1 = plt.figure(facecolor='w')
ax = fig1.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t1, S1/10000000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t1, I1/10000000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t1, R1/10000000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (10.000.000s)')
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

# Simulacao numero 2, uma simulacao basica do COVID no mundo dia 02/11/2020.

# Populacao no mundo
N2 = 7822785840 

# Numeros iniciais de infectados e recuperados.
I2, R2 = 46643798, 31156914

# Suscetiveis a contaminacao.
S2 = N2 - I2 - R2

# Taxas tecnicas.
beta2, gamma2 = 0.73, 0.64/10 

# Rede de tempo.
t2 = np.linspace(0, 100, 100) 

# Equacoes diferenciais do modelo SIR.
def deriv(y2, t2, N2, beta2, gamma2):
    S2, I2, R2 = y2
    dSdt2 = -beta2 * S2 * I2 / N2
    dIdt2 = beta2 * S2 * I2 / N2 - gamma2 * I2
    dRdt2 = gamma2 * I2
    return dSdt2, dIdt2, dRdt2

# Condicoes inicias do vetor.
y2 = S2, I2, R2

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret2 = odeint(deriv, y2, t2, args=(N2, beta2, gamma2))
S2, I2, R2 = ret2.T

# Plotando a simulacao.
fig2 = plt.figure(facecolor='w')
ax = fig2.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t2, S2/100000000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t2, I2/100000000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t2, R2/100000000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (100.000.000s)')
ax.set_ylim(0,80)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulacao numero 3, uma simulacao basica do COVID no mundo dia 02/11/2020 com a quarentena obedecida

# Populacao inicial ficticia.
N3 = 7822785840 

# Numeros iniciais de infectados e recuperados.
I3, R3 = 46643798, 31156914

# Suscetiveis a contaminacao.
S3 = N3 - I3 - R3

# Taxas tecnicas.
beta3, gamma3 = 0.2, 0.64/10 

# Rede de tempo.
t3 = np.linspace(0, 150, 150)

# Equacoes diferenciais do modelo SIR.
def deriv(y3, t3, N3, beta3, gamma3):
    S3, I3, R3 = y3
    dSdt3 = -beta3 * S3 * I3 / N3
    dIdt3 = beta3 * S3 * I3 / N3 - gamma3 * I3
    dRdt3 = gamma3 * I3
    return dSdt3, dIdt3, dRdt3

# Condicoes inicias do vetor.
y3 = S3, I3, R3

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret3 = odeint(deriv, y3, t3, args=(N3, beta3, gamma3))
S3, I3, R3 = ret3.T

# Plotando a simulacao.
fig3 = plt.figure(facecolor='w')
ax = fig3.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t3, S3/100000000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t3, I3/100000000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t3, R3/100000000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (100.000.000ss)')
ax.set_ylim(0,80)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulacao numero 4, uma simulacao de Hepatite A em um hospital entre 2007 e 2008

# Populacao inicial
N4 = 1630

# Numeros iniciais de infectados e recuperados.
I4, R4 = 1396, 0

# Suscetiveis a contaminacao.
S4 = N4 - I4 - R4

# Taxas tecnicas.
beta4, gamma4 = 0.62, 0.81/10 

# Rede de tempo.
t4 = np.linspace(0, 50, 50)

# Equacoes diferenciais do modelo SIR.
def deriv(y4, t4, N4, beta4, gamma4):
    S4, I4, R4 = y4
    dSdt4 = -beta4 * S4 * I4 / N4
    dIdt4 = beta4 * S4 * I4 / N4 - gamma4 * I4
    dRdt4 = gamma4 * I4
    return dSdt4, dIdt4, dRdt4

# Condicoes inicias do vetor.
y4 = S4, I4, R4

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret4 = odeint(deriv, y4, t4, args=(N4, beta4, gamma4))
S4, I4, R4 = ret4.T

# Plotando a simulacao.
fig4 = plt.figure(facecolor='w')
ax = fig4.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t4, S4/100, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t4, I4/100, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t4, R4/100, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (100s)')
ax.set_ylim(0,16)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulacao numero 5, uma simulacao de dengue no sudoeste da Bahia em 2012

# Populacao na regiao
N5 = 225530

# Numeros iniciais de infectados e recuperados.
I5, R5 = 166521, 0

# Suscetiveis a contaminacao.
S5 = N5 - I5 - R5 

# Taxas tecnicas.
beta5, gamma5 = 0.75, 0.2/10 

# Rede de tempo.
t5 = np.linspace(0, 365, 365) 

# Equacoes diferenciais do modelo SIR.
def deriv(y5, t5, N5, beta5, gamma5):
    S5, I5, R5 = y5
    dSdt5 = -beta5 * S5 * I5 / N5
    dIdt5 = beta5 * S5 * I5 / N5 - gamma5 * I5
    dRdt5 = gamma5 * I5
    return dSdt5, dIdt5, dRdt5

# Condicoes inicias do vetor.
y5 = S5, I5, R5

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret5 = odeint(deriv, y5, t5, args=(N5, beta5, gamma5))
S5, I5, R5 = ret5.T

# Plotando a simulacao.
fig5 = plt.figure(facecolor='w')
ax = fig5.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t5, S5/1000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t5, I5/1000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t5, R5/1000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (1000s)')
ax.set_ylim(0,250)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulacao numero 6, uma simulacao da H1N1 no Brasil em 2009.

# Populacao inicial.
N6 = 193900000 

# Numeros iniciais de infectados e recuperados.
I6, R6 = 4, 0

# Suscetiveis a contaminacao.
S6 = N6 - I6 - R6

# Taxas tecnicas.
beta6, gamma6 = 2.7, 2/10 

# Rede de tempo.
t6 = np.linspace(0, 60, 60)

# Equacoes diferenciais do modelo SIR.
def deriv(y6, t6, N6, beta6, gamma6):
    S6, I6, R6 = y6
    dSdt6 = -beta6 * S6 * I6 / N6
    dIdt6 = beta6 * S6 * I6 / N6 - gamma6 * I6
    dRdt6 = gamma6 * I6
    return dSdt6, dIdt6, dRdt6

# Condicoes inicias do vetor.
y6 = S6, I6, R6

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret6 = odeint(deriv, y6, t6, args=(N6, beta6, gamma6))
S6, I6, R6 = ret6.T

# Plotando a simulacao.
fig6 = plt.figure(facecolor='w')
ax = fig6.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t6, S6/1000000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t6, I6/1000000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t6, R6/1000000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (1.000.000s)')
ax.set_ylim(0,200)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

##############################################################################

# Simulacao numero 7, uma simulacao basica do COVID no início da pandemia

# Populacao inicial ficticia.
N7 = 7822785840 

# Numeros iniciais de infectados e recuperados.
I7, R7 = 1, 0

# Suscetiveis a contaminacao.
S7 = N7 - I7 - R7

# Taxas tecnicas.
beta7, gamma7 = 0.73, 0.64/10 

# Rede de tempo.
t7 = np.linspace(0, 150, 150)

# Equacoes diferenciais do modelo SIR.
def deriv(y7, t7, N7, beta7, gamma7):
    S7, I7, R7 = y7
    dSdt7 = -beta7 * S7 * I7 / N7
    dIdt7 = beta7 * S7 * I7 / N7 - gamma7 * I7
    dRdt7 = gamma7 * I7
    return dSdt7, dIdt7, dRdt7

# Condicoes inicias do vetor.
y7 = S7, I7, R7

# Integracao do modelo de equacoes diferenciais do SIR na rede de tempo(t).
ret7 = odeint(deriv, y7, t7, args=(N7, beta7, gamma7))
S7, I7, R7 = ret7.T

# Plotando a simulacao.
fig7 = plt.figure(facecolor='w')
ax = fig7.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t7, S7/100000000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t7, I7/100000000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t7, R7/100000000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
ax.set_xlabel('Tempo /dias')
ax.set_ylabel('Número (100.000.000ss)')
ax.set_ylim(0,80)
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
    #https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/
    #https://www.ibge.gov.br/apps/populacao/projecao/; 
    #https://www.gazetadopovo.com.br/republica/breves/taxa-de-recuperacao-da-covid-19-e-maior-no-brasil-que-espanha-italia-e-eua/;
    #https://g1.globo.com/bemestar/coronavirus/noticia/2020/10/13/taxa-de-transmissao-da-covid-19-fica-abaixo-de-1-pela-terceira-semana-seguida-no-brasil-aponta-imperial-college.ghtml
    #http://www.uberaba.mg.gov.br/portal/conteudo,49499
    #https://www.prefeitura.sp.gov.br/cidade/secretarias/saude/vigilancia_em_saude/doencas_e_agravos/coronavirus/index.php?p=291766
    #https://news.google.com/covid19/map?hl=pt-BR&gl=BR&ceid=BR%3Apt-419
    #https://www.worldometers.info/pt/
    #https://agenciabrasil.ebc.com.br/saude/noticia/2020-08/taxa-de-transmissao-da-covid-19-no-brasil-cai-para-101-diz-estudo
    #https://veja.abril.com.br/brasil/covid-19-taxa-de-recuperados-no-brasil-e-maior-do-que-a-mundial/
    #https://www.paho.org/pt/covid19
    #https://covid19.who.int/table
    #https://ciis.fmrp.usp.br/covid19/epcalc/public/index.html
    #https://towardsdatascience.com/modelling-the-coronavirus-epidemic-spreading-in-a-city-with-python-babd14d82fa2
    #https://www.ime.usp.br/~map/tcc/2015/Rafael%20Belmiro.pdf
    #http://scielo.iec.gov.br/scielo.php?script=sci_arttext&pid=S2176-62232010000200013
    #https://www.scielo.br/scielo.php?script=sci_arttext&pid=S2179-84512014000300003
    #https://eadcampus.spo.ifsp.edu.br/pluginfile.php/197454/mod_resource/content/0/TCC%20ALINE%20DE%20OLIVEIRA%20VIEIRA-mesclado_rearranged.pdf
    #http://www.blog.saude.gov.br/index.php/53845-10-anos-do-surto-global-de-h1n1
    
##############################################################################