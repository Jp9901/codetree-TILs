n, b = map(int,input().split())

info = [list(map(int, input().split())) for _ in range(n)]

# info.sort(key=lambda x:(sum(x))
# print(info)

# i번째 선물의 가격에 쿠폰
max_cnt = 0
for i in range(n):
    # i번째 선물의 가격에 쿠폰
    cost = info[i][0]//2 + info[i][1]
    cnt = 1

    # i번째 선물을 제외한 새 리스트 => 합의 크기 순으로 정렬
    new_info = [info[idx] for idx in range(n) if idx != i]
    new_info.sort(key = lambda x:sum(x))

    for j in range(n-1):
        # i번째 선물을 제외하고
        if i == j:
            continue
        # 나머지는 선물+배송비가 싼 순으로 하나씩 추가
        
        
        cost += sum(new_info[j])

        if cost > b:
            break
        cnt += 1

    
    max_cnt= max(max_cnt,cnt)

print(max_cnt)