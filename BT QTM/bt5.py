class chuoi:
	def __init__(self):
		self.s = ""
	def getString(self):
		self.s = str(input("Nhập: "))
	def printString(self):
		print("Chuỗi: ", self.s)
	def vietHoa(self):
		self.s = self.s.upper()
an = chuoi()
an.getString()
an.printString()
an.vietHoa()
an.printString()