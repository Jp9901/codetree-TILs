n = int(input())

li = list(map(int, input().split()))

# 쌍의 수
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        if li[i] <= li[j]:
            for k in range(j+1,n):
                if li[j] <= li[k]:
                    cnt += 1

print(cnt)