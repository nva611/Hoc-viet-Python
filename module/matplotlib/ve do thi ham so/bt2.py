#y = x**2
import matplotlib.pyplot as plt
import numpy as np 

fx = lambda x : x**2 
x = np.arange(-10, 10.01, 0.01)
y = [fx(i) for i in x]

plt.plot(x, y, 'g-')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Đồ thị hàm số y = x^2')

plt.show()

