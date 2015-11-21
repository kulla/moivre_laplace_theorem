import matplotlib.pyplot as plt
import numpy as np
import os

from scipy.stats import norm, binom

p = 0.25
q = 1-p
n = 1000
h = 1 / np.sqrt(n*p*q)

ks = np.arange(0., n+1, 1.)
xs = ( ks - n * p ) * h

sel = (xs > -5) & (xs < 5)
ks = ks[sel]
xs = xs[sel]

plt.plot(xs, binom.pmf(ks, n, p) - norm.pdf(xs) * h)
plt.plot(xs, (q-p)/6 * (xs**3-3*xs) * norm.pdf(xs) * h**2)
plt.legend( ("$f(x_k)$", "$g(x_k)$") )
plt.xlabel("$x_k$")
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
