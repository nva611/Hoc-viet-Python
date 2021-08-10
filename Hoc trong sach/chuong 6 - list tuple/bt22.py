A = [1, 2, 3, 7, 1, 3, 5, 6, 3, 1, 9, 2]
def xoa(A):
	x = int(input("Nhập số cần xóa: "))
	for i in range(0, A.count(x)):
		A.remove(x)
print(A)
xoa(A)
print(A)
