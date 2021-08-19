# y = sin x
import matplotlib.pyplot as plt 
import numpy as np 
fx = lambda x : np.sin(x)
x = np.arange(-10, 10, 0.01)
y = [fx(i) for i in x]

plt.figure('VẼ ĐỒ THỊ',figsize = (10,5), edgecolor = 'r', dpi = 80, facecolor = 'g', linewidth = 5)
plt.plot(x, y, 'b-')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Đồ thị hàm số y = sin x')

plt.show()