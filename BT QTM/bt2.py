n = int(input())
def giaiThua(x):
	if x==1 or x==0:
		return 1
	return x*giaiThua(x-1)
print(giaiThua(n))