n,m,k = tuple(map(int,input().split()))  #이동횟수, 목표점, 말의 수
move=list(map(int,input().split()))      #이동거리

# k 1부터 k까지 for문
#[1, 1, 2, 2, 3, 3 ]
#이 리스트에 대한 for문으로 result=[0]*k 의 각 위치 값에 이동거리를 더해줌. 

from itertools import combinations_with_replacement as cwr
all=cwr([i+1 for i in range(k)],n)

aws=0
for a in all:
    result=[0]*k

    for i, coin in enumerate(a):
            result[coin-1]+=move[i]
    cnt=0
    for b in result:
        if b>=m:
            cnt+=1
    aws=max(cnt,aws)



if sum(move)<m:
    print(0)
else:
    print(aws)