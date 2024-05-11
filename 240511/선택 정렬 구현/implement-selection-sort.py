# 선택 정렬 함수
def sel_sort(front,rear):
    if front > rear:
        return rear, front
    else:
        return front,rear

n = int(input())
arr = list(map(int,input().split()))

for i in range(n-1):
    val = arr[i]

    # i번째 이후의 최솟값
    rear_val = min(arr[i+1:])
    rear_idx = arr.index(rear_val)

    arr[i], arr[rear_idx] = sel_sort(arr[i],arr[rear_idx])

print(*arr)