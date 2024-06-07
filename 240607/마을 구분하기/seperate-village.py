#어떤 점을 입력하면 그 마을의 크기를 기록하는 dfs함수를 모든 점에 대해 반복
#각 크기를 리스트에 저장
#dfs함수는 다녀온 점의 값을 0으로 바꿈. 


n=int(input())
graph=[list(map(int,input().split()))for _ in range(n)]
record=[[False]*n for _ in range(n)]

dxs,dys=[0,-1,0,1],[1,0,-1,0]

def can_go(x,y):
    if 0<=x<n and 0<=y<n and graph[x][y]==1 :
        return True

def dfs(x,y):
    
    cnt=1
    record[x][y]=True
    graph[x][y]=0

    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if can_go(nx,ny) and not record[nx][ny]:
            
            
            cnt+=dfs(nx,ny)
    return cnt

aws=[]
for x in range(n):
    for y in range(n):
        if graph[x][y]==1:
            aws.append(dfs(x,y))

print(len(aws))

aws.sort()
for i in range(len(aws)):
    print(aws[i])