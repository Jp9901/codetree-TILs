n=int(input())


dp=[0]*(n+10)

dp[1]=2
dp[2]=7

for i in range(3,n+1):
    dp[n]=2*dp[n-1]+3*dp[n-2]


print(dp[n]%1000000007)