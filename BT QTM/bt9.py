from math import sqrt
C = 50
H = 30
value = []
items = [d for d in input().split(',')]
print(items)
for D in items:
	value.append(str(int(round(sqrt(2*C*float(D)/H)))))
print(', '.join(value))