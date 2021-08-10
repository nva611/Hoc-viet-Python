from decimal import Decimal
pos_inf = Decimal('Infinity')
neg_inf = Decimal('-Infinity')
s = str(input("Nhập dãy số cách nhau bởi dấu cách: "))
A = s.split(" ")
X = []
for i in A:
	X.append(int(i))
X.append(pos_inf)
X.insert(0, neg_inf)
T = X.copy()
L = X.copy()
def dayConTangNhat(X, T, L):
	l = len(X)
	T[l-1] = 0
	for i in range(l-2, -1, -1):
		max_index = l-1
		for j in range(l-1, i, -1):
			if X[i]<X[j] and T[j]>T[max_index]:
				max_index = j
		T[i] = T[max_index] + 1
		L[i] = max_index
def xuat(X, T, L):
	x = X[0]
	l = L[0]
	while l!=len(X)-1:
		print(X[l])
		l = L[l]
dayConTangNhat(X, T, L)
xuat(X, T, L)


