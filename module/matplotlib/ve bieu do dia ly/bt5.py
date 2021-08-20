# NỢ NƯỚC NGOÀI CỦA MỘT SỐ QUỐC GIA MĨ LA TINH, NĂM 2017 (Đơn vị: Tỉ USD)
# Quốc gia			Nợ nước ngoài
# Ac-hen-ti-na		236.5
# Braxin			543.0
# Ê-cua-đo			41.1
# Ha-mai-ca			14.7
# Mê-hi-cô			441.6
# Pa-ra-goay		15.9
# Pê-ru				67.6
# Vê-nê-xu-ê-la		148.9

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8,6))

col_names = ['Ac-hen-ti-na', 'Braxin', 'Ê-cua-đo', 'Ha-mai-ca', 'Mê-hi-cô', 'Pa-ra-goay', 'Pê-ru', 'Vê-nê-xu-ê-la']

data = [236.5, 543, 41.1, 14.7, 441.6, 15.9, 67.6, 148.9]

index = np.arange(8)
width = 0.3
plt.bar(index, data, width, color = 'black')

plt.xlabel('Tên nước')
plt.ylabel('Tỉ USD')

plt.title('TÌNH HÌNH NỢ NƯỚC NGOÀI CỦA MỘT SỐ QUỐC GIA MĨ LA TINH, NĂM 2017', fontcolor = 'red')

plt.xticks(index, col_names)

plt.show()