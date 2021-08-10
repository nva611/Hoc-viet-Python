def cauA(X):
	m = len(X)
	for i in range(m-1):
		if X[i] > X[i+1]:
			return False
	return True
def cauB(X):
	m = len(X)
	for i in range(m-1):
		if X[i] >= X[i+1]:
			return False
	return True
def cauA(X):
	m = len(X)
	for i in range(m-1):
		if X[i] < X[i+1]:
			return False
	return True
def cauA(X):
	m = len(X)
	for i in range(m-1):
		if X[i] <= X[i+1]:
			return False
	return True
