n = int(input("Nhập số n: "))
def UocSo(x):
	for i in range(1, x+1):
		if x%i==0:
			print(i, end = " ")
UocSo(n)