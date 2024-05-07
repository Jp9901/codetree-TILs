n = int(input())

info = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
# i번째에 조약돌이 넣었을 때,
for i in range(1,4):
    li = [0]*(n+1)
    li[i] = 1
    cnt = 0

    for a,b,c in info:
        li[a], li[b] = li[b],li[a]

        if li[c] == 1:
            cnt += 1
        
    max_cnt = max(max_cnt, cnt)

print(max_cnt)