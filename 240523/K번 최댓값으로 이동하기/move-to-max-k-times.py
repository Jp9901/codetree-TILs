#출발점을 입력하면 도착점을 반환하는 bfs함수를 정의한다
#bfs함수:

#
#bfs함수를 k번 반복한다. 
n,k=tuple(map(int,input().split()))
graph= [list(map(int,input().split())) for _ in range(n)]
r,c=tuple(map(int,input().split()))
r,c=r-1,c-1                                                    #1행 1열을 graph[0][0]으로 표현한다. 

from collections import deque
dxs,dys=[0,1,0,-1],[1,0,-1,0]

def can_go(x,y,nx,ny,visit):
    p=tuple([nx,ny])
    if 0<=nx<n and 0<=ny<n and (p not in visit) and graph[x][y]>graph[nx][ny]:
        return True
    else:
        return False


def bfs(point):
    visit=set()
    visit.add(point)
    q=deque([point])

    aws=tuple([-1,-1])
    big_value=0

    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            npoint=tuple([nx,ny])

            if can_go(x,y,nx,ny,visit):
                visit.add(npoint)
                q.append(npoint)
                value=graph[nx][ny]
                if value>big_value:
                    big_value=value
                    aws=tuple([nx,ny])
                if big_value==value:       #두 좌표를 비교해야하는데
                    if aws[0]== nx:        #행번호가 같다면 열번호가 더 작은 점으로 저장
                        if aws[1]<ny:
                            aws=aws
                        else:
                            aws=tuple([nx,ny])
                    else:                  #행번호가 다르다면 행번호가 더 작은 점으로 저장
                        if aws[0]<nx:
                            aws=aws
                        else: 
                            aws=tuple([nx,ny])
                        

    if aws==tuple([-1,-1]):
        return point
    else:
        return aws

p=tuple([r,c])
for _ in range(k):
    p=bfs(p)

print(p[0]+1,end=' ')
print(p[1]+1)