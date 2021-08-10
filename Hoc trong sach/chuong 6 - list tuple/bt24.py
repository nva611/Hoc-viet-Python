a = [1,2,3,4]
b = [5,6,7,8,9]
c = []
for i in range(len(a)):
	x = a.pop()
	c.append(x)
for i in range(len(b)):
	x = b.pop()
	c.append(x)
print(c)