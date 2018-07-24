import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.special import logit
plt.style.use('seaborn-darkgrid')
x = np.linspace(0.0001, 0.9999, 500)
mus = [0., 0., 0., 1.]
sds = [0.3, 1., 2., 1.]
for mu, sd in  zip(mus, sds):
    pdf = st.norm.pdf(logit(x), loc=mu, scale=sd) * 1/(x * (1-x))
    plt.plot(x, pdf, label=r'$\mu$ = {}, $\sigma$ = {}'.format(mu, sd))
    plt.legend(loc=1)
plt.show()