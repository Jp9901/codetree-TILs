n, m = map(int, input().split())

A = list(map(int,input().split()))

# a1 ~ a2번째 합계 함수 
def cal(a1,a2):
    return sum(A[(a1-1):a2])    

for i in range(m):
    a1, a2 = map(int,input().split())
    print(cal(a1,a2))