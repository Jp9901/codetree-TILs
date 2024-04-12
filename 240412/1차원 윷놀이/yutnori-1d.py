#K개 중 하나를 N번 선택하기(Conditional) / 1차원 윷놀이,                                        백트래킹
n,m,k = tuple(map(int,input().split()))  #이동횟수, 목표점, 말의 수
move=list(map(int,input().split()))      #이동거리

# k 1부터 k까지 for문
#[1, 1, 2, 2, 3, 3 ]
#이 리스트에 대한 for문으로 result=[0]*k 의 각 위치 값에 이동거리를 더해줌. 

from itertools import combinations_with_replacement as cwr
from itertools import permutations

all_1=cwr([i+1 for i in range(k)],n)

aws=0
for all in all_1:
    for a in permutations(all,n):
        result=[1]*k

    for i, coin in enumerate(a):
            result[coin-1]+=move[i]
    cnt=0
    for b in result:
        if b>=m:
            cnt+=1
    aws=max(cnt,aws)
    

print(aws)

# if sum(move)<m:
#     print(0)
# else:
#     print(aws)