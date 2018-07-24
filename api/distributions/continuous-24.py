import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-10, 20, 200)
mus = [0., 4., -1.]
betas = [2., 2., 4.]
for mu, beta in zip(mus, betas):
    pdf = st.gumbel_r.pdf(x, loc=mu, scale=beta)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $\beta$ = {}'.format(mu, beta))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()