import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.linspace(0, 1, 200)
a_s = [.5, 5., 1., 2., 2.]
b_s = [.5, 1., 3., 2., 5.]
for a, b in zip(a_s, b_s):
    pdf = a * b * x ** (a - 1) * (1 - x ** a) ** (b - 1)
    plt.plot(x, pdf, label=r'$a$ = {}, $b$ = {}'.format(a, b))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0, 3.)
plt.legend(loc=9)
plt.show()