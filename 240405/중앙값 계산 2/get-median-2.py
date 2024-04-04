import statistics
n=int(input())

list1=list(map(int, input().split()))

for i in range(n+1):
    if i%2==1:
        print(statistics.median(list1[:i]),end=' ')