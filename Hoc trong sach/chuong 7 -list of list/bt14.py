def nhap(X):
	m = int(input("Nhập số hàng: "))
	n = int(input("Nhập số cột: "))
	for i in range(m):
		row = []
		for j in range(n):
			x = int(input("Nhập giá trị ô [{}][{}]".format(i, j)))
			row.append(x)
		X.append(row)
def xuat(X):
	m = len(X)
	for i in range(m):
		for j in range(len(X[i])):
			print(X[i][j], end = " ")
		print()
def Scalar(A, k):
	X = []
	for item in A:
		X.append(item.copy())  #copy là tạo ra 1 bản sao khác, chú ý đến việc copy cả list có chứa list, lúc này các phần tử list cùng trỏ đến chung 1 ô nhớ của list mẹ. append là cùng trỏ đến ô nhớ. 
	m = len(X)
	for i in range(m):
		for j in range(len(X[i])):
			X[i][j] *= k
	return X
A = []
nhap(A)
k = float(input("Nhập k: "))
C = Scalar(A, k)
xuat(A)
xuat(C)