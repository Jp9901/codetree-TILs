n = int(input())

arr = [
    list(map(int,input().split())) for _ in range(n)
]

# x:-100~100, y:-100~100 좌표계
xy = [['empty' for _ in range(201)] for _ in range(201)]

# 정사각형 넓이 1의 위치(x~(x+1),y~(y+1)) 값을 (x,y)에 저장
for k in range(n):
    x1,y1,x2,y2 = arr[k]
    # 좌표 조정
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    for i in range(x1,x2):
        for j in range(y1,y2):
            if k%2 == 0:
                xy[i][j] = 'red'
            else:
                xy[i][j] = 'blue'

cnt = 0
for i in range(len(xy)):
    for j in range(len(xy)):
        if xy[i][j] == 'blue':
            cnt += 1

print(cnt)