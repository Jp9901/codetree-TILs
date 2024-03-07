A = input()
B = input()

n = len(A)

cnt = 0
for i in range(n-1):
    if B == A[i:i+2]:
        cnt += 1

print(cnt)