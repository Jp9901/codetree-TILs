n,m=tuple(map(int,input().split()))
graph=[[] for _ in range(n+1)]
dist=[[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=tuple(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
    dist[a][b]=c
    dist[b][a]=c


def dfs(x,target,value):
    if x==target:
        return value
    visit[x]=True
    for nei in graph[x]:
        if visit[nei]==False:
            result= dfs(nei,target,value+dist[x][nei])
            if result is not None:
                return result



for _ in range(m):
    visit=[False]*(n+1)
    a,b=tuple(map(int,input().split()))
    print(dfs(a,b,0))