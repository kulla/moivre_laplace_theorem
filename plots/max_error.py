import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

def max_error(p):
    def error(n):
        ks = np.arange(0, n+1, 1.)
        xs = ( ks - n * p ) / np.sqrt(n*p*(1-p))

        return np.abs( binom.cdf(ks, n, p) - norm.cdf(xs) ).max()


    ns = np.arange(1, 1001, 1)
    return (np.vectorize(error)(ns) * np.sqrt(ns)).max()

ps = np.arange(0.02, 0.99, 0.02)

plt.plot(ps, np.vectorize(max_error)(ps))
plt.plot(ps, 0.4215 * (ps**2+(1-ps)**2) / np.sqrt(ps*(1-ps)))
plt.legend(("f(p)", "g(p)"))
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
