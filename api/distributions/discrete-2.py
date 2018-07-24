import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy import special
plt.style.use('seaborn-darkgrid')

def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

x = np.arange(0, 11)
alphas = [0.5, 1, 2.3]
betas = [0.5, 1, 2]
n = 10
for a, b in zip(alphas, betas):
    pmf = BetaBinom(a, b, n, x)
    plt.plot(x, pmf, '-o', label=r'$\alpha$ = {}, $\beta$ = {}, n = {}'.format(a, b, n))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0)
plt.legend(loc=9)
plt.show()