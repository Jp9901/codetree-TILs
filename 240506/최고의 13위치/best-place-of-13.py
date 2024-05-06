n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]
# print(li)

cnt = 0
max_cnt = cnt
for i in range(n):
    for j in range(n-2):
        cnt = sum(li[i][j:j+3])
        # print(li[i][j:j+3])
        # print(cnt)
        if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)