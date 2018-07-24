import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-10, 10, 1000)
mus = [0.,  0., 0.]
sds = [3.,5.,7.]
a1 = [-3, -5, -5]
b1 = [7, 5, 4]
for mu, sd, a, b in zip(mus, sds,a1,b1):
    print mu, sd, a, b
    an, bn = (a - mu) / sd, (b - mu) / sd
    pdf = st.truncnorm.pdf(x, an,bn, loc=mu, scale=sd)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $\sigma$ = {}, a={}, b={}'.format(mu, sd, a, b))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()