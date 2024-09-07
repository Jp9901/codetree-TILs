n=int(input())
prices=list(map(int, input().split()))
import sys
min_p=sys.maxsize
max_d=-1

for price in prices:
    min_p=min(price,min_p)

    diff=price-min_p

    max_d=max(max_d,diff)

print(max_d)