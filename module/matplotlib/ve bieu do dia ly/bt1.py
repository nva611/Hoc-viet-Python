# LƯỢNG MƯA TRUNG BÌNH THÁNG Ở THÀNH PHỐ HỒ CHÍ MINH (Đơn vị: mm)
# Tháng        1       2      3      4      5      6      7      8      9      10     11     12
# Lượng mưa   13.8    4.1    10.5   50.4   218.4  311.7  293.7  269.8   327   266.7  116.5  48.3
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (9,7))
col_names = ['1','2','3','4','5','6','7','8','9','10','11','12']
data = [13.8, 4.1, 10.5, 50.4, 218.4, 311.7, 293.7, 269.8, 327, 266.7, 116.5, 48.3]


plt.bar(col_names, data, color = 'green')
plt.title('BIỂU ĐỒ THỂ HIỆN LƯỢNG MƯA TRUNG BÌNH THÁNG Ở THÀNH PHỐ HỒ CHÍ MINH')

plt.xlabel('Tháng')
plt.ylabel('Lượng mưa. đv : mm')
plt.show()