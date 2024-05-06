li = list(map(int,input().split()))
li.sort()

sum_val = sum(li)
min_diff = sum_val

for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1,5):
            team1 = li[i]+li[j]
            team2 = li[k]
            team3 = sum_val-team1-team2

            if team1!=team2 and team1!=team3 and team2!=team3:
                diff = max(team1,team2,team3)-min(team1,team2,team3)
                min_diff = min(min_diff,diff)

if min_diff == sum_val:
    print(-1)
else:
    print(min_diff)