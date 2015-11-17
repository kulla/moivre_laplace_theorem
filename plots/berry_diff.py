import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 100

xs= np.arange(-2.5, 2.51, 0.1)
ks= np.floor(n*p+xs*np.sqrt(n*p*q))

plt.plot(xs, binom.cdf(ks, n, p)- norm.cdf(xs), ".")
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
