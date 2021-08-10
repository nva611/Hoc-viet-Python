s = input()
d = {'hoa': 0, 'thuong': 0}
for i in s:
	if i.isupper():
		d['hoa'] += 1
	elif i.islower():
		d['thuong'] += 1
	else:
		pass
print("Số chữ hoa:", d['hoa'])
print("Số chữ thường:", d['thuong'])