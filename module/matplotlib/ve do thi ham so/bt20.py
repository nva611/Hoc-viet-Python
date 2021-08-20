# subplot
# y = 3x+5
# y = sin(3x) - cos(2x)

import matplotlib.pyplot as plt
import numpy as np
plt.figure(edgecolor = 'r', linewidth = 2, facecolor = 'b', figsize = (7,5))
f1 = lambda x : 3*x + 5
f2 = lambda x : np.sin(3*x)  - np.cos(2*x)

x = np.arange(-10, 10.01, 0.01)

y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]

plt.subplot(2,1,1)
plt.plot(x, y1, 'g-')
plt.title('y = 3x + 5')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2,1,2)
plt.plot(x, y2, 'r-')
plt.title('y = sin(3x) - cos(2x)')
plt.xlabel('x')
plt.ylabel('y')

plt.suptitle('Vẽ đồ thị')

plt.show()