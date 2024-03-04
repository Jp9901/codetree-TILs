n = int(input())

print("* "*n)
for i in range(1,n-1):
    print("* "*i,"  "*(n-1-i),sep='',end='')
    print("*")

print("* "*n)