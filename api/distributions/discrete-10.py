import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
ls = [1, -2]
us = [6, 2]
for l, u in zip(ls, us):
    x = np.arange(l, u+1)
    pmf = [1 / (u - l)] * len(x)
    plt.plot(x, pmf, '-o', label='lower = {}, upper = {}'.format(l, u))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0, 0.4)
plt.legend(loc=1)
plt.show()