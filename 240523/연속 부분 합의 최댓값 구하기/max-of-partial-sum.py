n = int(input())
arr = [0]+list(map(int,input().split()))

dp = [0]*(n+1)

# 초기값
dp[1] = arr[1]

for i in range(2,n+1):
    dp[i] = max(dp[i-1]+arr[i],arr[i])

print(dp[n])