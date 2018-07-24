import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.arange(0, 22)
psis = [0.7, 0.4]
thetas = [8, 4]
for psi, theta in zip(psis, thetas):
    pmf = st.poisson.pmf(x, theta)
    pmf[0] = (1 - psi) + pmf[0]
    pmf[1:] =  psi * pmf[1:]
    pmf /= pmf.sum()
    plt.plot(x, pmf, '-o', label='$\\psi$ = {}, $\\theta$ = {}'.format(psi, theta))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()