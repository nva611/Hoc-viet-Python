def fa(m, n):
	dem = 0
	for i in range(1, m*(m<n) + n*(n<=m)+1):
		if m%i==0 and n%i==0:
			dem = dem + 1
	return dem
def fb(m, n):
	dem = 0
	for i in range (1, m+1):
		if m%i==0 and n%i!=0:
			dem = dem + 1
	return dem
def fc(m, n):
	tong = 0
	for i in range(1, m*(m<n) + n*(n<=m)+1):
		if m%i==0 and n%i==0:
			tong = tong + i
	return tong
print(fa(10, 20), fb(10,20), fc(10, 20), sep = "\n", end ="")
