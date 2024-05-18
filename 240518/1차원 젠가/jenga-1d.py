n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

s1,e1 = map(int,input().split())
del arr[(s1-1):e1]
s2,e2 = map(int,input().split())
del arr[(s2-1):e2]

print(len(arr))
for val in arr:
    print(val)