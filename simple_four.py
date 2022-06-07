import math

import matplotlib.pyplot as plt

x = [i * 0.2 for i in range(50)]
y = [math.sin(xi) for xi in x]
y2 = [math.cos(xi) for xi in x]
y3 = [0.2 * xi for xi in x]

plt.plot(x,y, 'r-')
plt.plot(x,y2, 'bo')
plt.plot(x,y3, 'g:')
plt.legend(['$sin(x)$', '$cos(x)$', '$0.2x$'])
plt.show()