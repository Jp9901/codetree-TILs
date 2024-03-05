arr = list(map(int,input().split()))

if arr[-1] == 0:
    arr.pop()

for ele in arr[::-1]:
    print(ele, end = " ")