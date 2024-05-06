import sys


n,h,t = map(int, input().split())
info = list(map(int,input().split()))


min_cost = sys.maxsize
# 1 ~ (N-T)번째를 시작점으로
for i in range(n-t+1):
    cost = 0

    # T번 이상 H 높이
    for j in range(i,i+t):
        cost += abs(info[j]-h)
   
    min_cost = min(min_cost,cost)

print(min_cost)