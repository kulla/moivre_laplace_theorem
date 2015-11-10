import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 1000

ks = np.arange(0., n+1, 1.)
xs = ( ks - n * p ) / np.sqrt(n*p*q)

plt.plot(xs, binom.pmf(ks, n, p))
