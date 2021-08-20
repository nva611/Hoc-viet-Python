# SẢN LƯỢNG LỢN CỦA NƯỚC TA VÀ MỘT SỐ VÙNG, NĂM 2010 VÀ NĂM 2016 (Đơn vị: Nghìn con)
# Cả nước/Vùng \ Năm		2010		2016
# Cả nước					27373,3		29075,3
# Đồng bằng sông Hồng		7301,0 		7414,4
# Đồng bằng sông Cửu Long	3798,9 		3803,0

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10,6))

col_names = ['Cả nước', 'ĐBSH', 'ĐBSCL']

index = np.arange(3)
width = 0.2

data_2010 = [27373.3, 7301, 3798.9]
data_2016 = [29075.3, 7414.4, 3803]

plt.bar(index, data_2010, width, color = 'pink', label = 'Năm 2010')
plt.bar(index + width, data_2016, width, color = 'blue', label = 'Năm 2016')

plt.xlabel('Vùng')
plt.ylabel('Nghìn con')
plt.title('BIỂU ĐỒ THỂ HIỆN TÌNH HÌNH CHĂN NUÔI LỢN Ở VÙNG DBSH, DBSCL, CẢ NƯỚC, NĂM 2010 VÀ NĂM 2016')
plt.xticks(index + width/2, col_names)

plt.legend(loc = 'best')

plt.show()