n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


# 범위 안에 들어있는 동전 개수
def num_coin(r,c):
    cnt = 0

    for i in range(r,r+3):
        for j in range(c, c+3):
            cnt += arr[i][j]

    return cnt

max_cnt = 0
# 완전탐색
for row in range(n):
    for col in range(n):

        # 3*3 격자가 n*n 격자를 벗어날때
        if row+2 >= n or col+2 >= n:
            continue

        max_cnt = max(num_coin(row,col),max_cnt)

print(max_cnt)