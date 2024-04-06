#전체 격자를 만들고 값을 입력받아 색을 칠한다
#만약 편안한 상태가 true이면 1을 출력한다. 

#편안한 상태 함수
#좌표 두개를 입력받으면 벽이아니고and값이 1인 칸 이 총 3개일 때 True. 

N,M =tuple(map(int,input().split()))

aws=[[0]*N for _ in range(N)]

dxs,dys=[0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

def check(x,y):
    cnt=0
    for dx, dy in zip(dxs,dys):
        nx, ny=x+dx, y+dy 
        if in_range(nx,ny) and aws[nx][ny]==1:
            cnt+=1 

    if cnt==3:
        return True
    else: 
        return False

for _ in range(M):
    a,b=tuple(map(int,input().split()))
    aws[a-1][b-1]=1
    if check(a-1, b-1):
        print(1)
    else:
        print(0)