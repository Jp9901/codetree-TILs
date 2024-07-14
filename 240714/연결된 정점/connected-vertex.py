n,m=tuple(map(int,input().split()))

uf=[0]*(n+1)
for i in range(1,n+1):
    uf[i]=i

def find(x):
    if uf[x]==x:
        return x
    uf[x]=find(uf[x])
    return uf[x]

def union(x,y):
    X,Y=find(x),find(y)
    uf[X]=Y 


def x(a,b):
    union(a,b)

def y(k):
    mom=find(k)
    ans=0
    for i in range(1,n+1):
        if find(i)==mom:
            ans+=1
    print(ans)

        

for _ in range(m):
    command=input().split()
    if command[0]=="x":
        a,b=int(command[1]),int(command[2])
        x(a,b)
    else: 
        k=int(command[1])
        y(k)