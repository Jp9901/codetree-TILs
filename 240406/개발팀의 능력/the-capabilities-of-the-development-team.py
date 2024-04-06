from itertools import combinations
import sys
target=list(map(int, input().split()))
k=sum(target)

index=target
all=combinations(index,2) 
cnt=sys.maxsize

for all in all:                         #처음 2개의 인덱스
    index2=list(set(index)-set(all))    
    all2=combinations(index2,2)         #그다음 2개의 인덱스
       
    for all2 in all2:
        all3=list(set(index2)-set(all2))  #나머지 1개의 인덱스
        L=max(sum(all),sum(all2),sum(all3))
        l=min(sum(all),sum(all2),sum(all3))
        if (cnt > (L-l)) and (L!=(k-L-l)and l!=(k-L-l)):
            cnt=(L-l)

if cnt>5000:
    print(-1)
else:
    print(cnt)