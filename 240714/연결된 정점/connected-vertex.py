n,m=tuple(map(int,input().split()))

club=[1]*(n+1)
rank = [0] * (n + 1)  # 각 노드의 랭크를 저장


uf=[0]*(n+1)
for i in range(1,n+1):
    uf[i]=i

def find(x):
    if uf[x]==x:
        return x
    uf[x]=find(uf[x])
    return uf[x]

# def union(x,y):
#     X,Y=find(x),find(y)
#     uf[X]=Y 
#     club[Y]+=club[X]
    
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            uf[rootY] = rootX
            club[rootX] += club[rootY]
        elif rank[rootX] < rank[rootY]:
            uf[rootX] = rootY
            club[rootY] += club[rootX]
        else:
            uf[rootY] = rootX
            club[rootX] += club[rootY]
            rank[rootX] += 1  # 두 트리의 랭크가 같을 때 하나의 랭크를 증가시킵니다.

def y(k):                #k와 연결되어 있는 노드의 개수 출력 
    mom=find(k)
    print(club[mom])


for _ in range(m):
    command=input().split()
    if command[0]=="x":
        a,b=int(command[1]),int(command[2])
        union(a,b)
    else: 
        k=int(command[1])
        y(k)