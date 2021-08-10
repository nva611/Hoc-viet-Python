class QuadrilSquare:
	def __init__(self, w = 0, h = 0):
		self.w = w 
		self.h = h
	def perimeter(self):
		return 2*(self.w+self.h)
	def area(self):
		return self.w*self.h 
hcn = QuadrilSquare(2,3)
print(hcn.perimeter(), hcn.area())
hv = QuadrilSquare(4, 4)
print(hv.perimeter(), hv.area())