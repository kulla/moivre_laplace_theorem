import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 20

ks = np.arange(0., n+1, 1.)

xs1 = ( ks - n * p ) / np.sqrt(n*p*q)
xs2 = np.arange( np.min(xs1), np.max(xs1), 0.01 )

plt.plot(xs1, binom.cdf(ks, n, p), ".")
plt.plot(xs2, norm.cdf(xs2, 0, 1))
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
