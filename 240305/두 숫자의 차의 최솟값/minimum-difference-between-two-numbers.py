n = int(input())
arr = list(map(int,input().split()))

diff = list()
for i in range(n):
    for j in range(i+1,n):
        diff.append(abs(arr[i]-arr[j]))
print(min(diff))