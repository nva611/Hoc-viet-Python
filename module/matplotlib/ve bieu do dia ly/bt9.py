# biểu đồ cột chồng: Vẽ biểu đồ cột chồng thể hiện dân số thành thị và nông thôn ở TP. Hồ Chí Minh qua các năm. 
# Năm 			1995		2000		2002
# Nông thôn 	1174.3 		845.4 		855.8
# Thành thị 	3466.1 		4380.7 		4623.2

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10,8))

col_names = ['1995', '2000', '2002']

data_NongThon = [1174.3, 845.4, 855.8]
data_ThanhThi = [3466.1, 4380.7, 4623.2]

index = np.arange(3)
width = 0.2

plt.bar(index, data_NongThon, width, color = 'blue', label = 'Nông thôn', bottom = data_ThanhThi)
plt.bar(index, data_ThanhThi, width, color = 'red', label = 'Thành thị')

plt.xlabel('Năm')
plt.ylabel('Dân số (nghìn người)')
plt.xticks(index, col_names)
plt.title('BIỂU ĐỒ CỘT CHỒNG THỂ HIỆN DÂN SỐ THÀNH THỊ VÀ NÔNG THÔN Ở TP.HCM, GIAI ĐOẠN 1995 - 2002')
plt.legend(loc = 'best', title = 'Chú thích')

plt.show()