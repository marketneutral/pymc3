import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(0, 5, 200)
for sd in [0.4, 1., 2.]:
    pdf = st.halfnorm.pdf(x, scale=sd)
    plt.plot(x, pdf, label=r'$\sigma$ = {}'.format(sd))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()