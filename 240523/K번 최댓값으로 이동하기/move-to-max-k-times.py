n,k=tuple(map(int,input().split()))
graph= [list(map(int,input().split())) for _ in range(n)]
r,c=tuple(map(int,input().split()))
r,c=r-1,c-1                                                    #1행 1열을 graph[0][0]으로 표현한다. 

from collections import deque
dxs,dys=[0,1,0,-1],[1,0,-1,0]

def can_go(x,y,nx,ny,visit,start):
    p=tuple([nx,ny])
    if 0<=nx<n and 0<=ny<n and (p not in visit) and start>graph[nx][ny]:
        return True
    else:
        return False



def bfs(point):
    visit=set()
    visit.add(point)
    q=deque([point])

    start=graph[point[0]][point[1]]
    graph[point[0]][point[1]]=-1
    aws=point

    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            npoint=tuple([nx,ny])

            if can_go(x,y,nx,ny,visit,start):
                visit.add(npoint)
                q.append(npoint)
                

                if graph[nx][ny]>graph[aws[0]][aws[1]]:          #갱신대상을 최소화한다. 좌표만 갱신하면 값은 자동으로 갱신됨
                    graph[point[0]][point[1]]=start
                    aws=tuple([nx,ny])

                elif graph[nx][ny]==graph[aws[0]][aws[1]]:       #두 좌표를 비교해야하는데
                    if nx < aws[0] or (nx == aws[0] and ny < aws[1]):
                        aws=tuple([nx,ny])
                #print(graph[aws[0]][aws[1]])
                

    return aws if aws != point else None

p=tuple([r,c])
for _ in range(k):
    np=bfs(p)
    if np is None:
        break
    
    p=np

print(p[0]+1,end=' ')
print(p[1]+1)

#np=bfs(p)
#print(np)
# np=bfs(p,graph)
# print(np)
# np=bfs(np,graph)
# print(np)
# np=bfs(np,graph)
# print(np)