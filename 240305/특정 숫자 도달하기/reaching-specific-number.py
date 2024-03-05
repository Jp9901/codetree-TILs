arr = list(map(int,input().split()))
arr2 = list()

for ele in arr:
    if ele == 260:
        break
    arr2.append(ele)

print(sum(arr2), sum(arr2)/len(arr2))