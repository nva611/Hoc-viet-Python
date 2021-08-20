#subplot
#y = 2-x
# y = cos(3x)
# y = 3^x - 5

import matplotlib.pyplot as plt
import numpy as np

f1 = lambda x : 2-x
f2 = lambda x : np.cos(3*x)
f3 = lambda x : 3**x - 5

x = np.arange(-10, 10.01, 0.01)

y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
y3 = [f3(i) for i in x]

plt.subplot(2, 2, 1)
plt.plot(x, y1, 'b-')
plt.title('y = 2 - x')

plt.subplot(2, 2, 2)
plt.plot(x, y2, 'r-')
plt.title('y = cos(3x)')

plt.subplot(2, 2, 3)
plt.plot(x, y3, 'g-')
plt.title('y = 3^x - 5')

plt.suptitle('Vẽ đồ thị hàm số')
plt.show()