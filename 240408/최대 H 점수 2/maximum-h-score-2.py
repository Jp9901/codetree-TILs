# N개의 수니까, H점수는  2부터 N중에 하나이다.
# H점수가 n인지 확인하는 함수 check(n):
# n보다 크거나 같은게 n개라면 true
# n보다 1작은게 L개 이하라면 True 
# 아니면 False

N,L=tuple(map(int,input().split()))
numbers=list(map(int,input().split()))


def check(n):
    cnt_same=0
    for i in range(len(numbers)):
        if numbers[i]>=n :
            cnt_same+=1

    cnt_1=0
    for i in range(len(numbers)):
        if numbers[i]==(n-1) :
            cnt_1+=1

    if cnt_same>=n:
        return True
    elif (cnt_1<=L) and (cnt_same+cnt_1)>=n:
        return True
    else:
        return False

H=1
for h in range(2,N+1):
    if check(h):
        H=h
    else:
        break


print(H)