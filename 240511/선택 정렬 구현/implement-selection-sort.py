n = int(input())
arr = list(map(int,input().split()))

for i in range(n-1):

    # i번째 값 이후의 최솟값
    new_arr = arr[i+1:]
    min_val = min(new_arr)
    min_idx = (i+1)+new_arr.index(min_val)

    # i번째 값이 이후의 최솟값보다 크면,
    if arr[i] > min_val:
        # 교체
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    else:
        continue

print(*arr)