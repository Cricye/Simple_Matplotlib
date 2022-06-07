import math

import matplotlib.pyplot as plt

x = [i * 0.2 for i in range(50)]
y = [math.sin(xi) for xi in x]
y2 = [math.cos(xi) for xi in x]
y3 = [0.2 * xi for xi in x]

fig = plt.gcf()
fig.set_size_inches(12,4,forward=True)

plt.subplot(1,2,1)
plt.plot(x,y, 'r-')
plt.plot(x,y2, 'bo')

plt.subplot(1,2,2)
plt.plot(x,y3, 'g:')
plt.legend(['$sin(x)$', '$cos(x)$', '$0.2x$'])
plt.show()