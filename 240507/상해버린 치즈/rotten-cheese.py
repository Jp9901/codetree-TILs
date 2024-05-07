n,m,d,s = map(int,input().split())

# 어떤 사람(row)이 어떤 치즈(col)를 몇 초에 먹었는지
info = []
for _ in range(n):
    info.append([0]*m)

for _ in range(d):
    p,which,t = map(int,input().split())
    info[p-1][which-1] = t

info2 = [list(map(int,input().split())) for _ in range(s)]


# 아픈 사람이 아파지기 전에 먹은 치즈 찾기(먹은 치즈인 경우 +1)
cheese = [0] * m
for i, time in info2:
    for j in range(m):
        # 아프기 전에 먹은 치즈
        if time > info[i-1][j] and info[i-1][j] != 0:
            cheese[j] += 1
# => 상한 가능성이 있는 치즈의 값은 s

max_cnt = 0

# 먹은 치즈에 대해서
for i in range(m):
    # 아픈사람들이 먹지 않은 치즈
    if cheese[i] != s:
        continue
    
    # i번째 치즈(상한 치즈)를 먹은 사람의 수
    cnt = 0
    for j in range(n):
        if info[j][i] != 0:
            cnt += 1

    max_cnt = max(max_cnt,cnt)

print(max_cnt)