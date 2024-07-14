n,m=tuple(map(int,input().split()))

club=[]
for i in range(n+1):
    my_set={i}
    club.append(my_set)


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
    club[Y]|=club[X]
    #club[X]|=club[Y]


def y(k):                #k와 연결되어 있는 노드의 개수 출력 
    mom=find(k)
    print(len(club[mom]))


for _ in range(m):
    command=input().split()
    if command[0]=="x":
        a,b=int(command[1]),int(command[2])
        union(a,b)
    else: 
        k=int(command[1])
        y(k)