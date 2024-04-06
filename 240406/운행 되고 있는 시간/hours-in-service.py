N=int(input())
work=[list(map(int,input().split())) for _ in range(N)]
a=[max(i) for i in work]
k=max(a)

def check(l):
    cnt=0
    for i in range(len(l)):
        if l[i]>0:
            cnt+=1
    return cnt

aws=-1
for i in range(N):
    time=[0]*k
    for j in range(N):
        if i==j:
            continue
        x,y=tuple(work[j])
        for a in range(x,y):
            time[a]+=1
    z=check(time)
    aws=max(aws,z)

print(aws)