A = [[1,2,3], [4,5,6], [7,8,9]]
def ChangeRow(A, i, j):
	A[i], A[j] = A[j], A[i]
ChangeRow(A, 1,2)
print(A)