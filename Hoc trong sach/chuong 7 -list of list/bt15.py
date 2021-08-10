def nhap(X):
	m = int(input("Nhập số hàng: "))
	n = int(input("Nhập số cột: "))
	for i in range(m):
		row = []
		for j in range(n):
			x = int(input("Nhập giá trị ô [{}][{}]: ".format(i, j)))
			row.append(x)
		X.append(row)
def xuat(X):
	m = len(A)
	for i in range(m):
		for j in range(len(X[i])):
			print(X[i][j], end = " ")
		print()
def Multiple(A, B):
	X = []
	m = len(A)
	n = len(B)
	p = len(B[0])
	for k in range(m):
		row = []
		for h in range(p):
			kq = 0
			for i in range(n):
				kq += A[k][i] * B[i][h]
			row.append(kq)
		X.append(row)
	return X 
A = []
B = []
C = []
nhap(A)
nhap(B)
C = Multiple(A, B)
print(A, B, C)
xuat(C)
