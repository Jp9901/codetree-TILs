N=int(input())

check=[ int(input()) for _ in range(N)]

cnt=0
aws=[]
for i in range(N):
    
    if check[i]>check[i-1]:
        cnt+=1
        
    else:
        aws.append(cnt+1)
        cnt=0

print(max(aws))