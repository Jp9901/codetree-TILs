n = int(input())
arr = list(map(int,input().split()))

for i in range(1,n):
    val = arr[i]

    j = i-1
    # i번째 값보다 큰 수 앞에 배치
    while j>=0 and arr[j] > val:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        j -= 1

print(*arr)