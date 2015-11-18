import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 50

xs= np.arange(-2.5, 2.51, 0.02)
ks= np.floor(n*p+xs*np.sqrt(n*p*q))
xs2 = (ks - n*p) / np.sqrt(n*p*q)

plt.plot(xs, binom.cdf(ks, n, p)- norm.cdf(xs))
plt.plot(xs2, binom.cdf(ks, n, p)- norm.cdf(xs2))
plt.legend(("f(x)", "g(x_k)"))
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
