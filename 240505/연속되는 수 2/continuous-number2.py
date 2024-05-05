n = int(input())

li = list(int(input()) for _ in range(n))


cnt=1
max_cnt = cnt
for i in range(1,n):
    if li[i-1] == li[i]:
        cnt += 1
    if cnt > max_cnt:
        max_cnt=cnt




print(cnt)