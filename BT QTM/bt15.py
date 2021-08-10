value = []
for x in range(1000, 3001):
	i = str(x)
	if int(i[0])%2==0 and int(i[1])%2==0 and int(i[2])%2==0 and int(i[3])%2==0:
		value.append(i)
print(','.join(value))