#최소점프횟수가 n+1보다 크면 -1출력
#아니면 그대로 출력
##################################################################################

#10100101 이런 모든 순열을 구한다.(길이는 n-1인데 시작점이 1인 것만 남긴다)
#맨 끝에 2를 넣는다. (도착 확인)
#다음 1까지 이동할 수 없다면 break 
#이동할 수 있으면 위치를 계속 갱신한다. 


n=int(input())
move=list(map(int,input().split()))

from itertools import permutations
from itertools import combinations_with_replacement as cwr

# all_com=cwr([0,1], n-1)
# all_per=[]
# for com in all_com:
#     per=permutations(com,n-1)
#     for per in per:
#         if per[0]==1:
#             all_per.append(per)
        
# all_permu=[]
# for per in all_per:
#     per=list(per)
#     per.append(2)
#     all_permu.append(per)

all_permu = []
for i in range(2**(n-1)):
    bin_list = [int(x) for x in bin(i)[2:].zfill(n-1)]
    if bin_list[0] == 1:
        bin_list.append(2)  # 도착 지점을 의미하는 2 추가
        all_permu.append(bin_list)    
# del all_com,all_per

aws=2*n
for per in all_permu:      #[1,0,0,1,2]
    jump=0
    i=0        #현재 위치
    while True:
                        
        if per[i]==2:    #도착했다면
            aws=min(aws,jump)
            break
                                  
        if per[i]==0:
            break                #나아갈 수 없다면
        for k in range(1,n-i+1): #다음 1까지의 거리 구하기
            if per[k+i]!=0:
                dist=k
                break
        if k>move[i]:
            break
        else: 
            i+=k
            jump+=1

if aws>n+1:
    print(-1)
else:
    print(aws)