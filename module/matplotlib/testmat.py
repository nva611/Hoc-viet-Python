import matplotlib.pyplot as plt
import numpy as np
f = ['A', 'B', 'C', 'D', 'E']
mk = [20,25,15,10,20]
ex = [0,0.1,0.1,0.1,0.1]
plt.pie(mk, labels = f, shadow = True, startangle=45)
plt.axis('equal')
plt.legend(title = 'CT')
plt.show()