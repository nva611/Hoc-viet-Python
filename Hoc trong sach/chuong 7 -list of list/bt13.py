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
	m = len(X)
	for i in range(m):
		for j in range(len(X[i])):
			print(X[i][j], end = " ")
		print()
def Diff(A, B):
	X = []
	m = len(A)
	for i in range(m):
		row = []
		for j in range(len(A[i])):
			row.append(A[i][j] - B[i][j])
		X.append(row)
	return X
A = []
B = []
nhap(A)
nhap(B)
C = Diff(A, B)
xuat(C)