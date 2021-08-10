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

	@property
	def S(self):
		return self.__S
	@S.setter
	def S(self, s: int):
		self.__S = s

	def isTriange(self):
		if a+b>c or a+c>b or b+c>a:
			print("Là tam giác")
		else:
			print("Không là tam giác")
	
class Tam_giac(Triple):
	def __init__(self, a: int = 0, b: int = 0, c: int = 0):
		super().__init__(a, b, c)
	def banKinhNgoai(self):
		return (self.a*self.b*self.c)/(4*self.S)
	def banKinhNoi(self):
		self.S = (self.a+self.b+self.c)
		p = self.S/2
		dt = (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)
		return dt/self.S

tg = Tam_giac(2,5,132)
tg.a = 3
tg.b = 4 
tg.c = 5 
print(tg.a, tg.b, tg.c, tg.S)
print(tg.banKinhNoi())
print(tg.banKinhNgoai())