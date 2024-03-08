def sum_val_A(a1,a2):
    return sum(A[a1-1:a2])

n,m = tuple(map(int,input().split()))

A = list(map(int,input().split()))

for _ in range(m):
    a1,a2 = map(int,input().split())
    print(sum_val_A(a1,a2))