# n=int(input())
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# A.reverse()
# B.reverse()

# dp=[0]*n+1
# k=False

# for i in range(1,n+1):
#     if k==False:
#         if A[i]>B[i]:
#             dp[i]=B[i]+dp[i-1]
#             k=True
#         else:
#             dp[i]=dp[i-1]
#             k=False


#     else: 


def max_score(n, cards1, cards2):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 카드를 버리는 경우
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
            
            # 두 번째 플레이어가 점수를 얻는 경우
            if cards2[j-1] < cards1[i-1]:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + cards2[j-1])
    
    return dp[n][n]

# 입력 받기
n = int(input().strip())
cards1 = list(map(int, input().strip().split()))
cards2 = list(map(int, input().strip().split()))

# 결과 출력
print(max_score(n, cards1, cards2))