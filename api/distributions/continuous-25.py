import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-5, 5, 200)
mus = [0., 0., 0., -2.]
ss = [.4, 1., 2., .4]
for mu, s in zip(mus, ss):
    pdf = st.logistic.pdf(x, loc=mu, scale=s)
    plt.plot(x, pdf, label=r'$\mu$ = {}, $s$ = {}'.format(mu, s))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()