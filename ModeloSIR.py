import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10 
# A grid of time points (in days)
t = np.linspace(0, 160, 160)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
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

N1 = 27890
I1, R1 = 10, 0
S1 = N1 - I1 - R1
beta1, gamma1 = 0.4, 2./10 
t1 = np.linspace(0, 365, 365)
def deriv(y1, t1, N1, beta1, gamma1):
    S1, I1, R1 = y1
    dSdt1 = -beta1 * S1 * I1 / N1
    dIdt1 = beta1 * S1 * I1 / N1 - gamma1 * I1
    dRdt1 = gamma1 * I1
    return dSdt1, dIdt1, dRdt1

y1 = S1, I1, R1

ret1 = odeint(deriv, y1, t1, args=(N1, beta1, gamma1))
S1, I1, R1 = ret1.T

fig1 = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t1, S1/1000, 'b', alpha=0.5, lw=2, label='Suscetível')
ax.plot(t1, I1/1000, 'r', alpha=0.5, lw=2, label='Infectado')
ax.plot(t1, R1/1000, 'g', alpha=0.5, lw=2, label='Recuperado e imune')
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
