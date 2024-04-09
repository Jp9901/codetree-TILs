a,b,c=tuple(map(int,input().split()))

x=b-a
y=c-b

if x>=y:
    print(x-1)
else:
    print(y-1)