#visited 행렬은 F로 채우고 방문하면 T로 바꿈
#graph는 방문하면 0으로 바꿈. 
#count리스트에 dfs 리턴을 append함

#모든 graph의 값이 1인 좌표에 대해서 dfs를 실시
#dfs의 기능은 
#상하좌우 움직이면서 구멍을 파고, 파면
#visited, graph, cnt를 갱신함. 더 팔 수 없을 때 cnt를 리턴함. 

#인덱스는 0부터 n-1사용하기로 함

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

visited=[[False]*n for _ in range(n)]

index_list=[i for i in range(n)]
count=[]

def dfs(x,y,cnt):
    dxs,dys=[1,0,-1,0],[0,1,0,-1]
    
    for dx, dy in zip(dxs,dys):
        nx, ny= x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]==1 and visited[nx][ny]==False:
            graph[nx][ny]=0
            visited[nx][ny]=True
            
            cnt=dfs(nx,ny,cnt+1)

    return cnt


for x in index_list:
    for y in index_list:
        if graph[x][y]==1 and not visited[x][y]:
            
            a=dfs(x,y,0)
            count.append(a)

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])