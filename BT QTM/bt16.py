n = input()
d = {'chu': 0, 'so': 0}
for i in n:
	if i.isalpha():
		d['chu'] += 1
	elif i.isdigit():
		d['so'] += 1
	else:
		pass
print("Số chữ là:", d['chu'])
print("Số chữ số là:", d['so'])