m = 5
n = 10
a = [0 for i in range(m)]
b = [1 for i in range(n)]
a.extend(b)
print(a)