A = [0,1,2,3,4,5]
B = ['a', 'b', 'c']
def chen(A, B):
	k = int(input("Nhập vị trí chèn: "))
	C = A 
	B.reverse()
	for i in B:
		C.insert(k, i)
	return C
C = chen(A, B)
print(C)