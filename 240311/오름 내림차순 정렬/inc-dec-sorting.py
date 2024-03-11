n = int(input())
arr = list(map(int,input().split()))
arr.sort()

for ele in arr:
    print(ele, end =" ")
print()
for ele in arr[::-1]:
    print(ele, end= " ")