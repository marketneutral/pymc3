import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.arange(0, 25)
ns = [10, 20]
ps = [0.5, 0.7]
psis = [0.7, 0.4]
for n, p, psi in zip(ns, ps, psis):
    pmf = st.binom.pmf(x, n, p)
    pmf[0] = (1 - psi) + pmf[0]
    pmf[1:] =  psi * pmf[1:]
    pmf /= pmf.sum()
    plt.plot(x, pmf, '-o', label='n = {}, p = {}, $\\psi$ = {}'.format(n, p, psi))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()