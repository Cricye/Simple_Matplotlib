import matplotlib.pyplot as plt

x = [i * 0.2 for i in range(10)]
y = [xi ** 2 for xi in x]
y2 = [3 * xi -1 for xi in x]

plt.plot(x,y)
plt.plot(x,y2)
plt.ylim(0,5)
plt.xlabel('$x$ axis label')
plt.ylabel('$y$ axis label')
plt.title('$y=x^2$ and $y=3x-1$')
plt.legend(['$y=x^2$', '$y=3x-1$'])
plt.show()