n = int(input())
A = []
B = []
for i in range(n):
	if i%2==1:
		A.append(i)
	else:
		B.append(i)
print(A, B)