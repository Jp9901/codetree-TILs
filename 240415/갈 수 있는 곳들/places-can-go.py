n,k=tuple(map(int,input().split()))

graph=[list(map(int,input().split())) for _ in range(n)]   #그래프, 인덱스 0이 좌표1이다
points=[tuple(map(lambda x:x-1,map(int,input().split()))) for _ in range(k)]  #시작지점 튜플이 저장된 리스트 -1씩 해준다


from collections import deque

visit=set()

cnt=0

def bfs(point,graph):
    
    q=deque([point])
    
    if point in visit:
        local_cnt = 0
    else:
        local_cnt = 1
    visit.add(point)

    dxs,dys=[1,0,-1,0],[0,1,0,-1]
    while q:
        x, y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            npoint=tuple([nx,ny])
            if 0<=nx<n and 0<=ny<n and npoint not in visit and graph[nx][ny]==0:
                visit.add(npoint)
                local_cnt+=1
                q.append(npoint)

    return local_cnt

for p in points:
    cnt+=bfs(p,graph)

print(cnt)