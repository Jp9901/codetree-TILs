n = int(input())

if n == 1:
    print("*\n*")
else:
    print("* "*n)
    print("*")
    for i in range(n-1,1,-1):
        print("* "*i)
    for i in range(2,n):
        print("* "*i)
    print("*")
    print("* "*n)