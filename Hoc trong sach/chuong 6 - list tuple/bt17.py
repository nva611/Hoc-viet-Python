B = [1,2,3]
A = [9,8,7,6,5,4,3,2,1]
if len(A)<len(B):
	l = len(A)
	C = B
else:
	l = len(B)
	C = A
for i in range(0, l):
	C[i] = A[i] + B[i]
print(C)