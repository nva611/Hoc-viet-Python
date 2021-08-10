n = int(input("Nhập số n: "))
def DemSoUoc(x):
	dem = 0
	x = abs(x)
	for i in range(1, x+1):
		if x%i==0:
			dem = dem + 1
	return dem 
print(DemSoUoc(n))