import matplotlib.pyplot as plt
import numpy as np
import os

xs = np.arange(0.0, 1.0, 0.01)

plt.plot(xs, xs**3-1.5*xs**2+0.5*xs)
plt.savefig( os.path.splitext(__file__)[0] + ".pdf" )
