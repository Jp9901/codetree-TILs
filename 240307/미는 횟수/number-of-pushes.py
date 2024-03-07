A = input()
B = input()

len_A = len(A)

n = 0
for i in range(len_A):
    A = A[len_A-1]+A[:len_A-1]
    if A == B:
        n=i+1
        break

print(-1 if n==0 else n)