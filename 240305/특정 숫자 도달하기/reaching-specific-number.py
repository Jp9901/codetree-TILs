arr = list(map(int,input().split()))
arr2 = list()

for ele in arr:
    if ele >= 250:
        break
    arr2.append(ele)

print(f"{sum(arr2)} {sum(arr2)/len(arr2):.1f}")