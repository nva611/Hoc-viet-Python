class HocSinh:
	def __init__(self, hoVaTen: str = "", diaChi: str = "", chieuCao: str = "", canNang: str = "", hocLuc: str = ""):
		self.__hoVaTen = hoVaTen
		self.__diaChi = diaChi
		self.__chieuCao = chieuCao
		self.__canNang = canNang
		self.__hocLuc = hocLuc
	def show(self):
		s = "Tên: {}, Địa chỉ: {}, Chiều cao: {}, Cân nặng: {}, Học lực: {}".format(self.__hoVaTen,self.__diaChi, self.__chieuCao, self.__canNang, self.__hocLuc)
		print(s)

	@property
	def diaChi(self):
		return self.__diaChi
	@diaChi.setter
	def diaChi(self, s: str):
		if(s!=None):
			self.__diaChi = s

	@property
	def hoVaTen(self):
		return self.__hoVaTen
	@hoVaTen.setter
	def hoVaTen(self, s: str):
		if(s!=None):
			self.__hoVaTen = s 

	@property
	def chieuCao(self):
		return self.__chieuCao
	@chieuCao.setter
	def chieuCao(self, s:str):
		if(s!=None):
			self.__chieuCao = s

	@property
	def canNang(self):
		return self.__canNang
	@canNang.setter
	def canNang(self, s: str):
		if(s!=None):
			self.__canNang = s 
			
	@property
	def hocLuc(self):
		return self.__hocLuc
	@hocLuc.setter
	def hocLuc(self, s: str):
		if(s!=None):
			self.__hocLuc = s

an = HocSinh("nguyen van an", "Binh duong", "1m7", "56kg", "gioi")
an.diaChi = "Quảng Nam"
print(an.diaChi)
an.show()
