A = [1.2, "one", 0, 15, "A", 1, 25, 4.565231541545645645646, "z"]
B = []
for i in A:
	if type(i) == int or type(i) == float:
		B.append(i)
print(B)