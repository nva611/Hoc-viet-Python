s = int(input("Nhập số giây: "))
def doiRaGioPS(x):
	h, x = divmod(x, 3600)
	p, x = divmod(x, 60)
	return str(h)+' giờ',str(p) + ' phút',str(x) + ' giây'
for i in doiRaGioPS(s):
	print(i, end=' ')