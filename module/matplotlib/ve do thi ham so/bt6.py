# y = sin(2x) +2^x - 5
import matplotlib.pyplot as plt
import numpy as np

f = lambda x : np.sin(2*x) +2*x -5

x = np.arange(-10, 10.01, 0.01)
y = [f(i) for i in x]
plt.figure('ĐỒ THỊ HÀM SỐ', figsize = (7,10), edgecolor = 'r', linewidth = 2, facecolor = 'b', dpi = 85)

plt.plot(x, y, 'g-')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Đồ thị hàm số y = sin(2x) +2^x - 5')

plt.show()