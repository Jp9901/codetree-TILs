n, t = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

cnt = 0
tmp = 0
for i in range(n):
    if arr[i] > t:
        tmp += 1
        if tmp >= cnt:
            cnt = tmp
    else:
        tmp = 0

print(cnt)