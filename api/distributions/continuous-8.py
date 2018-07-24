import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-8, 8, 200)
mus = [0., 0., -2., -2.]
sds = [1., 1., 1., 2.]
dfs = [1., 5., 5., 5.]
for mu, sd, df in zip(mus, sds, dfs):
    pdf = st.t.pdf(x, df, loc=mu, scale=sd)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $\sigma$ = {}, $\nu$ = {}'.format(mu, sd, df))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()