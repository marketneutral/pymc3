import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy import special
plt.style.use('seaborn-darkgrid')

def ZeroInfNegBinom(a, m, psi, x):
    pmf = special.binom(x + a - 1, x) * (a / (m + a))**a * (m / (m + a))**x
    pmf[0] = (1 - psi) + pmf[0]
    pmf[1:] =  psi * pmf[1:]
    pmf /= pmf.sum()
    return pmf

x = np.arange(0, 25)
alphas = [2, 4]
mus = [2, 8]
psis = [0.7, 0.7]
for a, m, psi in zip(alphas, mus, psis):
    pmf = ZeroInfNegBinom(a, m, psi, x)
    plt.plot(x, pmf, '-o', label=r'$\alpha$ = {}, $\mu$ = {}, $\psi$ = {}'.format(a, m, psi))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()