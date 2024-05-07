n,k = map(int, input().split())
li = list(map(int,input().split()))

diff = max(li) - min(li)
cost = 0

# 최대 최소간의 차이가 k와 같아질때까지
while diff != k:
    max_val = max(li)
    max_n = li.count(max_val)
    min_val = min(li)
    min_n = li.count(min_val)
    
    # 최대 최소간의 차이가 k보다 클 때,
    if diff > k:
        # 최소값들의 개수가 더 많을 때, => 최대값을 움직임
        if min_n > max_n:
            for _ in range(max_n):
                li[li.index(max_val)] -= 1
                cost += 1
        # 그 외, => 최솟값을 움직임
        else : 
            for _ in range(min_n):
                li[li.index(min_val)] += 1
                cost += 1

    # 최대 최소간의 차이가 k보다 작을 때,
    elif diff < k:
        # 최소값들의 개수가 더 많을 때, => 최대값을 움직임
        if min_n > max_n:
            for _ in range(max_n):
                li[li.index(max_val)] += 1
                cost += 1
        # 그 외, => 최솟값을 움직임
        else : 
            for _ in range(min_n):
                li[li.index(min_val)] -= 1
                cost += 1

    diff = max(li) - min(li)

print(cost)