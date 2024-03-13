N,K,P,T = map(int, input().split())

arr = [
    list(map(int,input().split())) for _ in range(T)
]
arr.sort(key = lambda x:x[0])

dev = [0 for _ in range(N+1)]
dev[P] = 1

cnt = 0
for i, x, y in arr:
    if dev[x] == 1 or dev[y] == 1:
        dev[x] = 1
        dev[y] = 1
        cnt += 1
        if cnt == K:
            break

print(''.join(map(str,dev[1:])))