import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(0, 15, 200)
for df in [1, 2, 3, 6, 9]:
    pdf = st.chi2.pdf(x, df)
    plt.plot(x, pdf, label=r'$\nu$ = {}'.format(df))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0, 0.6)
plt.legend(loc=1)
plt.show()