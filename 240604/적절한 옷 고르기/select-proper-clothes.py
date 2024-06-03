n,m = map(int,input().split())

a = [[0]*n for _ in range(m+1)]

dp = [[0]*n for _ in range(m+1)]

# 행:i번째 날 / 열:j번 옷
for cl in range(n):
    s,e,v = map(int,input().split())
    for day in range(s,e+1):
        a[day][cl] = v



for day in range(2,m+1):
    # 전날 옷
    for cl1 in range(0,n):
        # 옷을 입을 수 없을 때,
        if a[day-1][cl1] == 0:
            continue

        # 오늘 옷
        for cl2 in range(0,n):
            # 옷을 입을 수 없을 때,
            if a[day][cl2] == 0:
                continue
            
            # 같은 옷을 입을 때,
            if cl1 == cl2:
                dp[day][cl2] = max(dp[day][cl2],dp[day-1][cl2]+0)
            # 다른 옷을 입을 때,
            else:
                #만족도 
                satis = abs(a[day-1][cl1]-a[day][cl2])
                dp[day][cl2] = max(dp[day][cl2], 
                dp[day-1][cl1]+satis)

print(max(dp[m]))