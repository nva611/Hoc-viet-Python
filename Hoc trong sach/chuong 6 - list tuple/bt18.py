s = str(input())
b = []
c = []
summ = 0
for i in s:
	if i.isdigit():
		b.append(i)
		summ += int(i)
dem = 0
for i in s:
	if i.isalpha():
		c.append(i)
		dem += 1
print(summ, dem)
print(b, c)