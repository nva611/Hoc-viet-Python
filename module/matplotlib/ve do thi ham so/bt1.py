# y = 2x
import matplotlib.pyplot as plt 
import numpy as np 

fx = lambda x: 2*x 
data = [fx(x) for x in range(-10, 11)]
index = np.arange(-10, 11)

plt.plot(data, index, 'r-')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Đồ thị hàm số y = 2x")

plt.show()