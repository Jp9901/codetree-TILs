n, t = tuple(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr = arr1
arr.extend(arr2)

for _ in range(t):
    tmp = arr[2*n-1]
    for i in range(2*n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = tmp

arr1 = arr[:n]
arr2 = arr[n:]
print(*arr1)
print(*arr2)