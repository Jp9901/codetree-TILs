n, b = map(int,input().split())

info = [list(map(int, input().split())) for _ in range(n)]

info.sort(key=lambda x:(x[0]//2,x[1]))
# print(info)

# i번째 선물의 가격에 쿠폰
max_cnt = 0
for i in range(n):
    cost = 0
    cnt = 0
    for j in range(n):
        # i번째 선물의 가격에 쿠폰
        if i == j:
            cost += info[j][0]//2 + info[j][1]
        # 나머지는 그대로
        else:
            cost += sum(info[j])
        # print(i,j,cost)
        if cost > b:
            break
        cnt += 1
        # print(cnt)
    
    max_cnt= max(max_cnt,cnt)

print(max_cnt)