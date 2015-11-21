import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

def slope(p):
    def error(n):
        ks = np.arange(0, n+1, 1.)
        h  = 1 / np.sqrt(n*p*(1-p))
        xs = ( ks - n * p ) * h

        return np.abs(binom.pmf(ks, n, p) - norm.pdf(xs) * h).max()


    ns = np.arange(500, 1000, 1)

    return np.polyfit( np.log(ns), np.log(np.vectorize(error)(ns)), 1 )[0]

ps = np.arange(0.02, 0.99, 0.02)

plt.plot(ps, np.vectorize(slope)(ps))
plt.ylim([-1.6, -0.9])
plt.xlabel("$p$")
plt.ylabel("convergence order")
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
