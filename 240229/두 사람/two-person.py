a = input().split()
b = input().split()

a1 = int(a[0])
a2 = a[1]

b1 = int(b[0])
b2 = b[1]

if (a2 == 'M' or b2 == 'M') and (a1>=19 or b1>=19):
    print(1)
else:
    print(0)