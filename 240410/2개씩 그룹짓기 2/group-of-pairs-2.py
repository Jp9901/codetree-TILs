#i부터 i+3의 차이를 계속 갱신하자. 
#i는 0부터 -4까지 탐색 

import sys
n=int(input())
numbers=list(map(int,input().split()))
numbers.sort()

value=sys.maxsize
for i in range(0,len(numbers)-n):
    value=min(value,abs(numbers[i]-numbers[i+n]))

print(value)