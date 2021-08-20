# GDP CỦA MA-LAI-XI-A VÀ XIN-GA-PO, GIẢI ĐOẠN 2010 - 2016 (Đơn vị: Tỷ đô la Mỹ)
# Năm			2010		2013		2016
# Ma-lai-xi-a   255			323			297
# Xin-ga-po		236			303			297

import matplotlib.pyplot as plt
import numpy as np

col_names = ['2010', '2013', '2016']
data_malay = [255, 323, 297]
data_xingapo = [236, 303, 297]

index = np.arange(3)
width = 0.3

plt.bar(index, data_malay, width, color = 'green', label = 'Ma-lai-xi-a')
plt.bar(index + width, data_xingapo, width, color = 'blue', label = 'Xin-ga-po')

plt.xlabel('Năm')
plt.ylabel('GDP, đơn vị: tỷ USD')
plt.title('QUY MÔ GDP CỦA MA-LAI-XI-A VÀ XIN-GA-PO, GIAI ĐOẠN 2010 - 2016')

plt.legend(loc = 'best')

plt.xticks(index + width/2, col_names)
plt.show()