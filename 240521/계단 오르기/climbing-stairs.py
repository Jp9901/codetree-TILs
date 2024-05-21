n=int(input())


dp=[-1]*(n+10)

dp[1]=0
dp[2]=1
dp[3]=1

#dp[n]=dp[n-2]+1 or dp[n-3]+1 if 0이 아니라면 


for i in range(4,n+1):
    dp[n]=dp[n-2]+ dp[n-3]

print(dp[n]%10007)