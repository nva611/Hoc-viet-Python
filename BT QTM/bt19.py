n = input().split(',')
sole = [x for x in n if int(x)%2!=0]
print(','.join(sole))