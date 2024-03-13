N,K,P,T = map(int, input().split())

arr = [
    list(map(int,input().split())) for _ in range(T)
]
arr.sort(key = lambda x:x[0])

dev = [0 for _ in range(N+1)]
dev[P] = 1

cnt = [0 for _ in range(N+1)]
for i, x, y in arr:
    if (dev[x]==1 and cnt[x]<=K) or (dev[y]==1 and cnt[y]<=K):
        dev[x] = 1
        cnt[x] += 1
        dev[y] = 1
        cnt[y] += 1

print(''.join(map(str,dev[1:])))