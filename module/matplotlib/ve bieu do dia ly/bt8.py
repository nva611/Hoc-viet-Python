# NHIỆT ĐỘ TRUNG BÌNH TẠI MỘT SỐ ĐỊA ĐIỂM (Đơn vị: 0C)
# Địa điểm		Nhiệt độ trung bình tháng I 		Nhiệt độ trung bình tháng VII 		Nhiệt độ trung bình năm
# Lạng Sơn 		13,3								27,0 								21,2
# Hà Nội		16,4								28,9								23,5
# Huế			19,7 								29,4								25,1
# Đà Nẵng		21,3 								29,1 								25,7
# Quy Nhơn		23,0 								29,7 								26,8
# TP.HCM 		25,8 								27,1 								26,9

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10,9))

col_names = ['Lạng Sơn', 'Hà Nội', 'Huế', 'Đà Nẵng', 'Quy Nhơn', 'TP.HCM']

data_tbI = [13.3,16.4,19.7,21.3,23,25.8]
data_tbVII = [27,28.9,29.4,29.1,29.7,27.1]
data_tbn = [21.2,23.5,25.1,25.7,26.8,26.9]

index = np.arange(6)
width = 0.2

plt.bar(index, data_tbI, width, color = 'green', label = 'Nhiệt độ trung bình tháng I')
plt.bar(index + width, data_tbVII, width, color = 'blue', label = 'Nhiệt độ trung bình tháng VII')
plt.bar(index + 2*width, data_tbn, width, color = 'black', label = 'Nhiệt độ trung bình năm')

plt.xlabel('Tỉnh/Thành phố')
plt.ylabel('Nhiệt độ, độ C')
plt.xticks(index + width, col_names)
plt.legend(loc = 'best')

plt.show()