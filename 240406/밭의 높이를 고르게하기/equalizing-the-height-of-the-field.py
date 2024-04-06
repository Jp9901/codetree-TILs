# 밭의 일부, T길이의 H높이를 가진 배열을 입력하면 고르게 만드는데 필요한 비용을
# 계산하는 합수 check를 정의한다, 

# 밭을 탐색하면서 check의 출력을 aws 값에 갱신한다. 

import sys
N,H,T= tuple(map(int, input().split()))
needed=list(map(int, input().split()))

problem=[H]*T

def check(needed, prob):
    cost=0
    for i in range(len(needed)):
        k=abs(needed[i]-prob[i])
        cost+=k
    return cost

cost=sys.maxsize
for i in range(N-T+1):
    a=check(needed[i:i+T],problem)
    cost=min(cost,a)

print(cost)