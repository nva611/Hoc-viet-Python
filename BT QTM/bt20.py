Money = {'D': 0, 'W': 0}
while True:
	s = input().split(' ')
	if s[0]=='D':
 		Money['D'] += float(s[1])
	elif s[0]=='W':
 		Money['W'] += float(s[1])
	else:
 		break
print('Tổng =', Money['D'] - Money['W'])