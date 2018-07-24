import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
plt.style.use('seaborn-darkgrid')
x = np.linspace(-2, 10, 500)
lowers = [0., -1, 2]
cs = [0.5, 0.5, 0.75]
uppers = [4., 2, 6]
for lower, c_, upper_ in zip(lowers, cs, uppers):
    pdf = st.triang.pdf(x, loc=lower, c=c_, scale=upper_)
    plt.plot(x, pdf, label='lower = {}, c = {}, upper = {}'.format(lower,
                                                                   lower + upper_ * c_,
                                                                   lower + upper_))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc=1)
plt.show()