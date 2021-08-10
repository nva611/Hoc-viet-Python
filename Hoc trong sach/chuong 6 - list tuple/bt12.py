from fractions import Fraction
n = int(input("Nhập n: "))
def a(x):
	sum = 0
	for i in range(1, x+1):
		sum += i**2
	return sum
def b(x):
	sum = 0
	for i in range(1, x+1):
		sum += Fraction(1, i)
	return sum
def c(x):
	sum = 0
	for i in range(2, x+1):
		sum += Fraction(1,(i-1)*i)
	return sum
print(a(n), b(n), c(n))