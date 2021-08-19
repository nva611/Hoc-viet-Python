# subplots 
# y = sin(x)^2 - 2
# y = (x^2 - 3x)
# y = x^2 - x^5
# y = cos(x) - 2^x

import matplotlib.pyplot as plt
import numpy as np

f1 = lambda x : np.sin(x)**2 - x
f2 = lambda x : (x**2 - 3*x)
f3 = lambda x : x**2 - x**5
f4 = lambda x : np.cos(x)-2*x

x = np.arange(-10, 10.01, 0.01)

y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
y3 = [f3(i) for i in x]
y4 = [f4(i) for i in x]

fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (5,5))

ax[0,0].plot(x, y1, 'g-')
ax[0,1].plot(x, y2, 'b-')
ax[1,0].plot(x, y3, 'r-')
ax[1,1].plot(x, y4, 'b-')

ax[0,0].set_title('y = sin(x)^2 - 2')
ax[0,1].set_title('y = x^2 - 3x')
ax[1,0].set_title('y = x^2 - x^5')
ax[1,1].set_title('y = cos(x) - 2^x')

plt.show()