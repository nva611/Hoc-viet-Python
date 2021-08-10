A = [1, 2, 3, 7, 1, 3, 5, 6, 3, 1, 9, 2]
def thay(X):
	k = int(input("Nhập số cần thay: "))
	m = int(input("Nhập giá trị thay: "))
	for i in range(0, X.count(k)):
		x = X.index(k)
		X[x] = m 
print(A)
thay(A)
print(A)