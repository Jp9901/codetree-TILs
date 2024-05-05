n, t = map(int, input().split())

li = list(map(int,input().split()))

cnt = 1
max_cnt = cnt
for i in range(1,n):
    if li[i-1] > t and li[i] > t:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)