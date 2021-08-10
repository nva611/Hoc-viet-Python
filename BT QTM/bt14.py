day_nhi_phan = input().split(',')
value = []
for i in day_nhi_phan:
	num = int(i, 2)
	if num%5==0:
		value.append(i)
print(','.join(value))