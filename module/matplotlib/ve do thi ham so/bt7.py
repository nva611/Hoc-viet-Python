# subplots
# y = 2x-7
# y = sin(2x) + 2x
# y = x^2 - 4x + 9
import matplotlib.pyplot as plt
import numpy as np
f1 = lambda x : 2*x - 7
f2 = lambda x : np.sin(2*x) + 2*x
f3 = lambda x : x**2 -4*x +9

x = np.arange(-10, 10.01, 0.01)

y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
y3 = [f3(i) for i in x]

fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (10,8))

ax[0,0].plot(x, y1,'r-')
ax[0,1].plot(x, y2, 'b-')
ax[1,0].plot(x, y3, 'g-')

ax[0,0].set_title('y = 2x-7')
#ax[0,0].set_xlabel('x')
ax[0,1].set_title('y = sin(2x) + 2x')
ax[1,0].set_title('y = x^2 - 4x + 9')

plt.show()