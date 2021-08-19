from math import sqrt
n = int(input("Nhập n: "))
A = [x for x in range(n+1) if x%2==0]
print(A)
B = [x**2 for x in range(1, (int(sqrt(n))+1)) if x**2 <= n]
print(B)