import matplotlib.pyplot as plt

x = [x * 0.1 for x in range(10)]
y = [y ** 2 for y in x]
print(['{0:0.2f}'.format(x) for x in x])
print(['{0:0.2f}'.format(x) for x in y])
# plt.plot((x,y))
plt.plot(x,y)
plt.show()