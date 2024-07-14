#코드트리 Intermediate High / MST / Disjoint Set (Union Find)

n,m=tuple(map(int,input().split()))

club=[1]*(n+1)                # 연결되어있는 노드집합 크기 저장
rank = [0] * (n + 1)          # 각 노드의 랭크를 저장


uf=[0]*(n+1)                  #uf 객체
for i in range(1,n+1):
    uf[i]=i

def find(x):                  #find 함수
    if uf[x]==x:
        return x
    uf[x]=find(uf[x])
    return uf[x]

def union(x,y):
    X,Y=find(x),find(y)
    if X!=Y:
        uf[X]=Y 
        club[Y]+=club[X]
    
# def union(x, y):              #랭크를 고려한 union함수 
#     rootX = find(x)
#     rootY = find(y)
    
#     if rootX != rootY:                            #두 부모가 다를때만 연결해줌 (불필요한 연산 없애기)
#         if rank[rootX] > rank[rootY]:             #둘중에 더 랭크가 큰것을 부모로 지정 (x가 클때)
#             uf[rootY] = rootX
#             club[rootX] += club[rootY]
#         elif rank[rootX] < rank[rootY]:           #(y가 클때)
#             uf[rootX] = rootY
#             club[rootY] += club[rootX]
#         else:                                     #(같을때)
#             uf[rootY] = rootX
#             club[rootX] += club[rootY]
#             rank[rootX] += 1                      # 두 트리의 랭크가 같을 때만 하나의 랭크를 증가시킵니다.


def y(k):                            #k와 연결되어 있는 노드의 개수 출력 
    mom=find(k)
    print(club[mom])


for _ in range(m):                   #문제에서 x일때는 노드연결, y일때는 연결노드집합크기 출력
    command=input().split()
    if command[0]=="x":
        a,b=int(command[1]),int(command[2])
        union(a,b)
    else: 
        k=int(command[1])
        y(k)