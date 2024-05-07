n,m = map(int, input().split())
li = [0]+list(map(int, input().split()))

max_cnt = 0
# 시작 위치
for i in range(1,n+1):
    cnt = 0
    # m번 움직임
    for _ in range(m):
        cnt += li[i]
        i = li[i]

    max_cnt = max(max_cnt,cnt)

print(max_cnt)