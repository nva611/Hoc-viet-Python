import matplotlib.pyplot as plt
import numpy as np

f = lambda x : np.sin(x) + x**2 - 5

x = np.arange(-10, 10.01, 0.01)
y = [f(i) for i in x]

plt.figure('ĐỒ THỊ HÀM SỐ', figsize = (15,15), edgecolor = 'r', linewidth = 4, facecolor = 'g', dpi = 80)

plt.plot([-10, 10],[0,0],'b-')
plt.plot([0,0], [-100, 100], 'b-')
plt.plot(x, y, 'g-')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Đồ thị hàm số y = sin(x) + x^2 - 5')

plt.show()