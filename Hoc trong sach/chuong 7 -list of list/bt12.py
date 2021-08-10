
def nhap(X):
	m = int(input("Nhập số hàng: "))
	n = int(input("Nhập số cột: "))
	for i in range(m):
		D = []
		for j in range(n):
			x = int(input("Nhập giá trị ô [{}][{}]: ".format(i, j)))
			D.append(x)
		X.append(D)
def cong(A, B):
	C = []
	for i in range(len(A)):
		D = []
		for j in range(len(A[i])):
			D.append(A[i][j] + B[i][j])
		C.append(D)
	return C
def xuat(X):
	for i in range(len(X)):
		for j in range(len(X[i])):
			print(X[i][j], end = " ")
		print()
A = []
B = []
nhap(A)
nhap(B)
print(A, B)
C = cong(A, B)
print("A")
xuat(A)
print("B")
xuat(B)
print("Tổng")
xuat(C)