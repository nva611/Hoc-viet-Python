s = str(input("Nhập dãy số cách nhau bởi dấu cách: "))
A = s.split(" ")
X = []
for i in A:
	X.append(int(i))
def dayTang(X):
	l = len(X)
	demDoDai = 0
	for i in range(l-1):
		dem = 0
		while X[i]<X[i+1]:
			dem += 1
			i += 1
		if dem >= demDoDai:
			demDoDai = dem 
			fn = i
	for i in range(fn-demDoDai+1, fn+1):
		print(X[i], end = " ")
dayTang(X)
