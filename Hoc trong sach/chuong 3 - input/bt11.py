day, month, year = eval(input("Nhap day, month, year cách nhau bởi dấu phẩy: "))
def laNamNhuan(x):
	if x%400==0 or (x%4==0 and x%100!=0):
		return True
	else:
		return False
def SoNgayTrongThang(m, y):
	Ngay =[31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if  laNamNhuan(y)==True and m==2:
		return Ngay[2]+1
	elif laNamNhuan(y)==False and m==2:
		return Ngay[2]
	else:
		return Ngay[m]
def tinhSoNgay(d, m, y):
	t = 0
	for i in range(1, m):
		t += SoNgayTrongThang(i, y)
	return t + d
print(tinhSoNgay(day, month, year))
	