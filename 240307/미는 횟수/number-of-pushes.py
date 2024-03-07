A = input()
B = input()

n = len(A)

cnt = 0
for i in range(n):
    A = A[1:]+A[0]
    cnt += 1
    if A == B:
        break

print(-1 if cnt == 0 else cnt)