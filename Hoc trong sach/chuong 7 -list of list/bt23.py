def GenPrime(x):
	for i in range(2, x+1):
		check = True
		for j in range(2, int(i**(1/2))+1):
			if i%j==0:
				check = False
				break
		if check==True:
			yield i
n = int(input("Nhập n: "))
for k in GenPrime(n):
	print(k)