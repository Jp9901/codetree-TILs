n = int(input())

li = list(int(input()) for _ in range(n))

# 각 횟수와 최대 횟수
cnt = 1
max_cnt = 1 
for i in range(1,n):
    if li[i-1]*li[i] > 0:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)