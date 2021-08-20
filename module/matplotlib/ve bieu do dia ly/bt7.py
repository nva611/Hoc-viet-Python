# GIÁ TRỊ XUẤT - NHẬP KHẨU CỦA NƯỚC TA, GIAI ĐOẠN 2010 - 2015 (Đơn vị: Triệu đô la Mỹ)
# Năm		2010		2013		2014		2015
# Xuất khẩu	72 236,7 	132 032,9 	150 217,1 	162 016,7
# Nhập khẩu 84 838,6 	132 032,6 	147 849,1 	165,775,9

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10,7))

col_names = ['2010', '2013', '2014', '2015']

index = np.arange(4)
width = 0.2

data_Xuat = [72236.7, 132032.9, 150217.1, 162016.7] 
data_Nhap = [84838.6, 132032.6, 147849.1, 165775.9]

plt.bar(index, data_Xuat, width, color = 'green', label = 'Xuất khẩu')
plt.bar(index + width, data_Nhap, width, color = 'blue', label = 'Nhập khẩu')

plt.xlabel('Năm')
plt.ylabel('Triệu đô la Mỹ')
plt.title('BIỂU ĐỒ THỂ HIỆN GIÁ TRỊ XUẤT - NHẬP KHẨU CỦA NƯỚC TA, GIAI ĐOẠN 2010 - 2015')
plt.xticks(index + width/2, col_names)

plt.legend(loc = 'best')

plt.show()