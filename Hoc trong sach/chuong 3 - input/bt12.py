import math
n = int(input("Nhập số n: "))
def laSoNguyenTo(x):
	if x<=1:
		return False
	elif x==2:
		return True
	for i in range (2, int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True
if laSoNguyenTo(n)==True:
	print(n, "la so nguyen to")
else:
	print(n, "KHONG la so nguyen to")