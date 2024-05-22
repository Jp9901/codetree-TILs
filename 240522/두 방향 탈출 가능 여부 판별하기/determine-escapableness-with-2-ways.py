n,m=map(int,input().split())
graph=[list(map(int,input().split()))  for _ in range(n)]
visit=[[False]*m for _ in range(n)]
visit[0][0]=True

dxs,dys=[0,1],[1,0]

def can_go(x,y,graph):
    if 0<=x<n and 0<=y<m and graph[x][y]==1:
        return True
    else: 
        return False


def dfs(x,y,graph):
    global a

    if x==n-1 and y==m-1:
        a=True
    
    else:
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny,graph):
                visit[nx][ny]=True
                dfs(nx,ny,graph)
        a=False

         

    

dfs(0,0,graph)

if a:
    print(1)
else:
    print(0)