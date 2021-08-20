# LƯỢNG MƯA, LƯỢNG BỐC HƠI VÀ CÂN BẰNG ẨM CỦA MỘT SỐ ĐỊA ĐIỂM Ở NƯỚC TA (Đơn vị: mm)
# Địa điểm 		Lượng mưa		Lượng bốc hơi		Cân bằng ẩm
# Hà Nội		1676			989					687
# Huế			2868			1000				1868
# TP HCM		1931			1686				245

import matplotlib.pyplot as plt
import numpy as np

col_names = ['Hà Nội', 'Huế', 'TP. Hồ Chí Minh']

data_HaNoi = [1676,989,687]
data_Hue = [2868,1000,1868]
data_TPHCM = [1931,1686,245]

index = np.arange(3)
width = 0.2

plt.figure(figsize = (8,7))

plt.bar(index, data_HaNoi, width, color = 'green', label = 'Hà Nội')
plt.bar(index + width, data_Hue, width, color = 'blue', label = 'Huế')
plt.bar(index + 2*width, data_TPHCM, width, color = 'red', label = 'TP. Hồ Chí Minh')

plt.xlabel('Địa điểm')
plt.ylabel('Lượng mưa, đơn vị: mm')
plt.title('LƯỢNG MƯA, LƯỢNG BỐC HƠI VÀ CÂN BẰNG ẨM CỦA MỘT SỐ ĐỊA ĐIỂM Ở NƯỚC TA')
plt.xticks(index + width, col_names)
plt.legend(loc ='best')

plt.show()