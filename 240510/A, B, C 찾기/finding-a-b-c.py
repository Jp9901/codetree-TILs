li = list(map(int,input().split()))
li.sort()

# 가장 작은 수 = A
# 다음 작은 수 = B
a = li[0]
b = li[1]

# 가장 큰 수 = A+B+C
c = li[-1] - a - b


print(a,b,c)