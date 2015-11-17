import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 1000
h = 1 / np.sqrt(n*p*q)

xs = np.arange(-5., 5.01, 0.25)
ks = np.floor(n*p + xs * np.sqrt(n*p*q))
rs = ks- (n*p+xs*np.sqrt(n*p*q)) + 0.5

plt.plot(xs, binom.cdf(ks, n, p) - norm.cdf(xs), "." )
plt.plot(xs, (q-p)/6 * (1-xs**2) * norm.pdf(xs) * h + norm.pdf(xs) * h * rs, ".")
plt.legend( ("f(z)", "g(z)") )
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
