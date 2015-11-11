import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 20

ks = np.arange(0., n+1, 1.)
xs = ( ks - n * p ) / np.sqrt(n*p*q)

plt.plot(xs, binom.pmf(ks, n, p), ".")
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
