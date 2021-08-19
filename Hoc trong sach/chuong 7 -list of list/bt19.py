s = str(input("Nhấp chuỗi 0 1 cách nhau bởi dấu cách: "))
A = s.split(" ")
X = []
for i in A:
	X.append(int(i))
demSo0 = 0
l = len(X)
for i in range(l):
	dem = 0 
	while i<l and X[i]==0 :
		dem += 1
		i += 1
	if dem > demSo0:
		demSo0 = dem
		st = i-dem
print(st, demSo0)
