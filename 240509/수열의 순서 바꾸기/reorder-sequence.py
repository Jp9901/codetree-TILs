n = int(input())
li = list(map(int,input().split()))

# 정렬된 수열
li_sort = sorted(li)

# 정렬
cnt = 0
while li != li_sort:
    first = li[0]

    # 맨 앞 숫자가 수열의 최댓값이면
    if first == max(li):
        # 맨 뒤로 보낸다
        li = li[1:] + [li[0]]

    # 맨 앞 숫자가 수열의 최솟값이면
    elif first == min(li):
        # 최댓값 뒤로 보낸다.
        max_idx = li.index(max(li))
        li = li[1:(max_idx+1)] + [li[0]] + li[(max_idx+1):]

    # 나머지 숫자는
    else:
        # 이전 수 뒤로 보낸다.
        num_idx = li.index(first-1)
        li = li[1:(num_idx+1)] + [li[0]] + li[(num_idx+1):]
    
    cnt += 1

print(cnt)