import math
def laSoNguyenTo(x):
	if (x<=1):
		return False
	elif x==2:
		return True
	for i in range(2, int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True
for i in range(1, 10000):
	if laSoNguyenTo(i):
		for j in range(i+1, 10_000):
			if laSoNguyenTo(j):
				if j-i==2:
					print("(", i,",", j,")")
				elif j-i>2:
					break