import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(0, 3, 200)
alphas = [.5, 1., 1.5, 5., 5.]
betas = [1., 1., 1., 1.,  2]
for a, b in zip(alphas, betas):
    pdf = st.weibull_min.pdf(x, a, scale=b)
    plt.plot(x, pdf, label=r'$\alpha$ = {}, $\beta$ = {}'.format(a, b))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0, 2.5)
plt.legend(loc=1)
plt.show()