A = [[1,2,3], [4,5,6], [7,8,9]]
def ChangeColumn(A, i, j):
	for k in range(len(A)):
		A[k][i], A[k][j] = A[k][j], A[k][i]
ChangeColumn(A,1,2)
print(A)