import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-6, 9, 200)
mus = [0., -2., 0., -3.]
sds = [1., 1., 3., 1.]
nus = [1., 1., 1., 4.]
for mu, sd, nu in zip(mus, sds, nus):
    pdf = st.exponnorm.pdf(x, nu/sd, loc=mu, scale=sd)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $\sigma$ = {}, $\nu$ = {}'.format(mu, sd, nu))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()