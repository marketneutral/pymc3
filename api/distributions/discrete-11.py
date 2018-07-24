import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.arange(1, 11)
for p in [0.1, 0.25, 0.75]:
    pmf = st.geom.pmf(x, p)
    plt.plot(x, pmf, '-o', label='p = {}'.format(p))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()