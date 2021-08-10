from math import sqrt
n = int(input("Nhập số lượng phần tử: "))
print("Nhập giá trị {} phần tử: ".format(n))
l = []
for i in range(0, n):
	l.append(int(input("+ Phần tử thứ {}: ".format(i))))
def laSoNguyenTo(x):
	if(x<=1):
		return False
	elif x==2:
		return True
	for i in range(2, int(sqrt(x))+1):
		if x%i==0:
			return False
	return True
kq = []
for i in l:
	if laSoNguyenTo(i):
		kq.append(i)
print(kq)