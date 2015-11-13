import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 1000

ks = np.arange(0., n+1, 1.)
xs = ( ks - n * p ) / np.sqrt(n*p*q)

sel = (xs > -5) & (xs < 5)

plt.plot(xs[sel], binom.cdf(ks[sel], n, p)- norm.cdf(xs[sel]))
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
