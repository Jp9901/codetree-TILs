import sys

n,m = map(int,input().split())
coins = list(map(int,input().split()))

dp =[10001]*(m+1)

dp[0] = 0
for i in range(1,m+1):
    for j in range(n):
        if i >= coins[j]:
            if dp[i-coins[j]] == -1:
                continue
            
            dp[i] = min(dp[i], dp[i-coins[j]]+1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])