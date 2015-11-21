import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

def slope(p):
    def error(n):
        ks = np.arange(0, n+1, 1.)
        xs = ( ks - n * p ) / np.sqrt(n*p*(1-p))

        return np.abs( binom.cdf(ks, n, p) - norm.cdf(xs) ).max()


    ns = np.arange(100, 1000, 1)

    return np.polyfit( np.log(ns), np.log(np.vectorize(error)(ns)), 1 )[0]

ps = np.arange(0.02, 0.99, 0.02)

plt.plot(ps, np.vectorize(slope)(ps))
plt.ylim([-0.8,-0.2])
plt.xlabel("$x$")
plt.ylabel("$\\alpha$")
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
