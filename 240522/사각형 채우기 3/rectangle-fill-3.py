n=int(input())


dp=[0]*(n+10)

dp[1]=2
dp[2]=7
dp[3]=22

for i in range(3,n+1):
    dp[i]=2*dp[i-1]+3*dp[i-2]+2*dp[i-3]


print(dp[n]%1000000007)