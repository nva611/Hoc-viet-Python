from matplotlib import pyplot as plt
plt.plot(range(5))
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.draw()
plt.show()