s=input().split()
b=int(s[0])
a=int(s[1])


for i in range(b,a-1,-1):
    if i%2==1:
        print(i,end=' ')