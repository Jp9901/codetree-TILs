N=int(input())


dp=[-1]*(N+10)

dp[1]=1
dp[2]=1

for i in range(3,N):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[N])