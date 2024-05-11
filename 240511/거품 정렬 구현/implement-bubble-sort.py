n = int(input())
arr = list(map(int,input().split()))

sort = False

while sort==False:
    sort = True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            sort = False

print(*arr)