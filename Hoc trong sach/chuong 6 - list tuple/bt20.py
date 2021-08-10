A = [1, "one", 6, "six", "seven", 7, 9, "nine", 3, 5, 2,"two", 4]
def sort(X):
	for i in range(1, len(X)):
		if type(X[i])!=str:
			key = X[i]
			k = i
			j = i-1
			while type(X[j])==str:
				j -= 1
			while X[j]>key and j>=0:
				X[k] = X[j]
				k = j
				j -= 1
				while type(X[j])==str:
					j -= 1
			X[k] = key
B = A
sort(B)
print(B)
