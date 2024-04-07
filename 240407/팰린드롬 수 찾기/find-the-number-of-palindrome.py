def check(k):
    number=list(map(int,str(k)))
    if len(number)%2==0:   #짝수일때
        a=len(number)//2
        for i in range(a):
            if number[i]!=number[-(i+1)]:
                return False
        else:
            return True
    else:
        a=(len(number)-1)//2
        for i in range(a):
            if number[i]!=number[-(i+1)]:
                return False
        else:
            return True



X,Y=tuple(map(int,input().split()))

cnt=0
for i in range(X,Y+1):
    if check(i):
        cnt+=1


print(cnt)