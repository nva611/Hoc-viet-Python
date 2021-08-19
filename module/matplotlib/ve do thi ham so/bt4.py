#y = x^3 - 2x^2 + 7
import matplotlib.pyplot as plt
import numpy as np

fx = lambda x : x**3 -2*x**2 + 7 
x = np.arange(-10, 10.01, 0.01)
y = [fx(i) for i in x]

plt.figure("VẼ ĐỒ THỊ HÀM SỐ", dpi = 90, edgecolor = 'r', linewidth = 2, facecolor = 'b', figsize = (10,5))

plt.plot(x, y, 'b-')

plt.xlabel('x')
plt.xlabel('y')
plt.title('Đồ thị hàm số y = x^3 - 2x^2 + 7')

plt.show()