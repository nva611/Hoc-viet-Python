# SẢN LƯỢNG GỖ KHAI THÁC CỦA CẢ NƯỚC VÀ MỘT SỐ VÙNG Ở NƯỚC TA, GIAI ĐOẠN 2012 - 2014 (Đơn vị: Nghìn m3)
# Năm \ Vùng 	Cả nước			Tây Nguyên		Trung du và miền núi Bắc Bộ
# 2012			5251			620				1590
# 2013			5908			540				1731
# 2014			7701			447				2278

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8,7))

col_names = ['2012', '2013', '2014']

data_CaNuoc = [5251,5908,7701]
data_TayNguyen = [620,540,447]
data_TDVMNBB = [1590,1731,2278]

index = np.arange(3)
width = 0.2

plt.bar(index, data_CaNuoc, width, color = 'green', label = 'Cả nước')
plt.bar(index + width, data_TDVMNBB, width, color = 'blue', label = 'TDVMNBB')
plt.bar(index + 2*width, data_TayNguyen, width, color = 'black', label = 'Tây Nguyên')


plt.xlabel('Năm')
plt.ylabel('Nghìn m^3')
plt.title('SẢN LƯỢNG GỖ KHAI THÁC CỦA CẢ NƯỚC VÀ MỘT SỐ VÙNG, GIAI ĐOẠN 2012 - 2014')

plt.xticks(index + width, col_names)
plt.legend(loc = 'best')

plt.show()