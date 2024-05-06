r,c = map(int,input().split())

li = [list(input().split()) for _ in range(r)]
# print(li)

# 시작 값
r0 = 0
c0 = 0
start = li[r0][c0]

# 경우 수
cnt = 0

# 조건2 : 오른쪽과 아래쪽으로 한 칸 이상 점프 => 첫 행, 첫 열, 마지막 행, 마지막 열 제외
# 조건3 : 시작과 도착 점 외에 두 번만 이동
# 첫번째 이동
for i in range(r0,r-1):
    for j in range(c0,c-1):

        # 조건1 : 다른 색으로 이동
        if start != li[i][j]:
            position = li[i][j] 
            # 두번째 이동
            for i_2 in range(i+1, r-1):
                for c_2 in range(j+1, c-1):
                    if position != li[i_2][c_2]:
                        cnt += 1
                
print(cnt)