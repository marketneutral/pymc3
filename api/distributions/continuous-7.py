import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-10, 10, 1000)
mus = [0., 0., 0., -5.]
bs = [1., 2., 4., 4.]
for mu, b in zip(mus, bs):
    pdf = st.laplace.pdf(x, loc=mu, scale=b)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $b$ = {}'.format(mu, b))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()