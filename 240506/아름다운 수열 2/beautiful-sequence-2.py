n,m = map(int,input().split())
li_A = list(map(int,input().split()))
li_B = list(map(int,input().split()))

# print(li_A,li_B)

cnt = 0
# 모든 구간의 시작점
for i in range(0,n-m+1):
    if sorted(li_A[i:i+m]) == sorted(li_B):
        cnt += 1

print(cnt)