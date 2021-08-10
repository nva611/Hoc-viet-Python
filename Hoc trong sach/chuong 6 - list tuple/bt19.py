A = [2,0,3,6,1,9,7,5,8,4]

def sort(X):
	for i in range(1, len(X)):
		key = X[i]
		j = i-1
		while X[j]>key and j>=0:
			X[j+1] = X[j]
			j -= 1
		X[j+1] = key
sort(A)
print(A)

