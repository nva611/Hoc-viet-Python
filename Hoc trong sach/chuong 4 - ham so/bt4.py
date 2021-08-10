from math import *
n = 10
def fa(n):
	dem = 0
	for i in range(1, n+1):
		if(n%i==0):
			dem = dem + 1
	return dem
def fb(n):
	if(n==1):
		return 0
	for i in range(2, int(sqrt(n)+1)):
		if(n%i==0):
			return 0
	return 1
def fc(n):
	dem = 0
	for i in range(1, n+1):
		if(n%i==0 and i%2==1):
			dem = dem + 1
	return dem
def fd(n):
	dem = 0
	for i in range(1, n+1):
		if(n%i==0 and fb(i)==1):
			dem = dem + 1
	return dem
def fe(n):
	t = 0
	for i in range(1, n+1):
		if(n%i==0):
			t += i
	return t
print(fa(n), fb(n), fc(n), fd(n), fe(n))
