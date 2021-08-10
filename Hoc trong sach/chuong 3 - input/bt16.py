n = int(input("Nhập số n: "))
def fa(x):
	return (2*x+1)*x
def fb(x):
	t = 0
	for i in range(1, n, 2):
		t += i
	return t 
def fc(x):
	t = 0
	for i in range(2, n, 2):
		t += i 
	return t 
print(fa(n), fb(n), fc(n))