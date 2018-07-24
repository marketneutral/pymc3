import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy import special
plt.style.use('seaborn-darkgrid')

def DiscreteWeibull(q, b, x):
    return q**(x**b) - q**((x + 1)**b)

x = np.arange(0, 10)
qs = [0.1, 0.9, 0.9]
betas = [0.3, 1.3, 3]
for q, b in zip(qs, betas):
    pmf = DiscreteWeibull(q, b, x)
    plt.plot(x, pmf, '-o', label=r'q = {}, $\beta$ = {}'.format(q, b))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0)
plt.legend(loc=1)
plt.show()