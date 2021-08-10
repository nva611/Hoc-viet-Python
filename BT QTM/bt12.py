list1 = []
while True:
	s = input()
	if s:
		list1.append(s.upper())
	else:
		break
for i in list1:
	print(i)