class Triple:
	def __init__(self, a: int = 0, b: int = 0, c: int = 0):
		self.__a = a 
		self.__b = b 
		self.__c = c 
		self.__S = a+b+c

	@property
	def a(self):
		return self.__a 
	@a.setter
	def a(self, a: int):
		if(a>0):
			self.__a = a

	@property
	def b(self):
		return self.__b
	@b.setter
	def b(self, b: int):
		if(b>0):
			self.__b = b 

	@property
	def c(self):
		return self.__c 
	@c.setter
	def c(self, c: int):
		if(c>0):
			self.__c = c 

	def isTriange(self):
		if a+b>c or a+c>b or b+c>a:
			print("Là tam giác")
		else:
			print("Không là tam giác")
tg = Triple(1,9,124)
a = 3
b = 4 
c = 5
tg.isTriange()