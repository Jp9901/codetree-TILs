n = int(input())
arr = list(map(int,input().split()))

arr1 = list()
for ele in arr:
    arr1.append(ele)
    arr1.sort()
    if len(arr1)%2 == 1:
        print(arr1[len(arr1)//2], end = " ")