n = int(input())
num = list(map(int,input().split()))

max_val = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            val = num[i]*num[j]*num[k]
            max_val = max(max_val,val)

print(max_val)