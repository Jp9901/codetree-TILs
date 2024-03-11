n = int(input())
arr = list()

for _ in range(n):
    arr.append(input())

arr.sort()
for ele in arr:
    print(ele)