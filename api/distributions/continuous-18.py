import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(0, 4, 1000)
alphas = [1., 2., 5., 5.]
ms = [1., 1., 1., 2.]
for alpha, m in zip(alphas, ms):
    pdf = st.pareto.pdf(x, alpha, scale=m)
    plt.plot(x, pdf, label=r'$\alpha$ = {}, m = {}'.format(alpha, m))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()