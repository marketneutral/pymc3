import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(0, 3, 500)
mus = [1., 1., 1., 3.]
lams = [1., .2, 3., 1.]
for mu, lam in zip(mus, lams):
    pdf = st.invgauss.pdf(x, mu/lam, scale=lam)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $\lambda$ = {}'.format(mu, lam))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()