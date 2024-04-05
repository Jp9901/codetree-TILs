N=int(input())

check=[ int(input()) for _ in range(N)]

cnt=1
aws=1
for i in range(1,N):
    
    if check[i]>check[i-1]:
        cnt+=1
        
    else:
        aws=max(aws,cnt)
        cnt=1

print(max(aws,cnt))