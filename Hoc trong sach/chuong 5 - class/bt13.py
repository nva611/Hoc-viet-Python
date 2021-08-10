from math import *
class CIRCLE:
	def __init__(self, a, b, c):
		self.R = a
		self.X = b
		self.Y = c
	def ChuVi(self):
		return 2*pi*self.R
	def DienTich(self):
		return pi*self.R**2
a = CIRCLE(2, 0, 0)
print(a.ChuVi())