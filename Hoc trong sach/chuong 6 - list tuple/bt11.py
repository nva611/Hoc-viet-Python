n = int(input("Nhập số lượng phần tử: "))
l = []
for i in range(0, n):
	l.append(int(input("+ Nhập giá trị phần tử thứ {}: ".format(i+1))))
sum = 0
for i in l:
	sum += i
print("Tổng = {}".format(sum))