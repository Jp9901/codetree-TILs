import sys

n,m = map(int,input().split())
coins = list(map(int,input().split()))

dp =[sys.maxsize]*(m+1)

dp[0] = 0
for i in range(1,m+1):
    for j in range(n):
        if i >= coins[j]:
            if dp[i-coins[j]] == -1:
                continue
            
            dp[i] = min(dp[i], dp[i-coins[j]]+1)

print(dp[m])