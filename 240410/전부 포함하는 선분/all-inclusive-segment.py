#최소선분의 길이를 구하는 함수를 정의한다 check
#튜플 리스트에 대해 반복하면서 나머지 선분들로 최소선분길이를 구한다
#최소선분길이를 갱신해서 최소값을 출력한다. 

n=int(input())
lines=[tuple(map(int,input().split())) for _ in range(n)]



def check(lis):
    lis_0=[a for (a,b) in lis]
    lis_1=[b for (a,b) in lis]
    a=min(lis_0)
    b=max(lis_1)
    return b-a

value=200
for i in range(n):
    res=lines[:i]+lines[i+1:]
    
  
    value=min(value,check(res))


print(value)