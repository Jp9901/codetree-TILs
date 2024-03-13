N = int(input())

arr =[
    int(input()) for _ in range(N)
]

cnt = 1
tmp = 1

for i in range(N):
    if i == 0:
        continue
    if arr[i]*arr[i-1]>0:
        tmp += 1
        if tmp >= cnt:
            cnt = tmp
    else:
        tmp = 1

print(cnt)