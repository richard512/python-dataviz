import numpy as np
import matplotlib.pyplot as plt

npoints = 10
b, a = np.mgrid[-5:5:npoints*1j, -1.5:1.5:npoints*1j]

z = a + b

fig, ax = plt.subplots()
im = ax.pcolormesh(a, b, z)
fig.colorbar(im)

ax.axis('tight')
plt.show()
