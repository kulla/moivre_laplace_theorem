import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25

def error(n):
    ks = np.arange(0, n+1, 1.)
    xs = ( ks - n * p ) / np.sqrt(n*p*(1-p))

    return np.abs( binom.cdf(ks, n, p) - norm.cdf(xs) ).max()

ns = np.arange(1, 1000, 1)

plt.plot(np.log(ns), np.log( np.vectorize(error)(ns) ))
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
