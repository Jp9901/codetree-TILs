n = int(input())
li = list(map(int,input().split()))

li.sort()

diff =[]
for i in range(n):
    j = n+i
    diff.append(abs(li[j]-li[i]))

print(min(diff))