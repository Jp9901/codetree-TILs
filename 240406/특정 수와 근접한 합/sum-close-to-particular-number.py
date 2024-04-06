from itertools import combinations
import sys
#리스트에 수들을 넣고 N-2개를 모두 뽑는 조합에 대해 합을 구하고 
#S와의 차이를 저장한다. 

N, S=tuple(map(int, input().split()))
numbers=list(map(int, input().split()))

com= combinations(numbers, N-2)

value=sys.maxsize
for com in com:
    if abs(sum(com)-S)<value:
        value=abs(sum(com)-S)


print(value)