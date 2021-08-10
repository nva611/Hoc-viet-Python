h = int(input("Nhap gio: "))
p = int(input("Nhap phut: "))
s = int(input("Nhap giay: "))
def tinh(h, p, s):
	return float(h)/24 + p/(24*60) + s/(24*60*60)
print(tinh(h, p, s))