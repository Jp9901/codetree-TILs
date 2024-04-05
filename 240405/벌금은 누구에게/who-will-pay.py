#벌칙을 하나씩 읽으면서 딕셔러니의 값을 1씩 더해주고
#값이 K가 되면 반복문을 멈추고 키를 출력
#벌칙을 모두 읽었는데 값이 K가 없으면 -1을 출력한다


N,M,K=tuple(map(int,input().split()))

#딕셔너리 생성
dic={i:0 for i in range(1,N+1) }

def check(dic):
    for i in range(1,N+1):
        if dic[i]==K:
            return i




aws=-1
for _ in range(M):
    x=int(input())
    dic[x]+=1
    if check(dic):
        aws=check(dic)
        print(aws)
        break

if aws==-1:
    print(-1)