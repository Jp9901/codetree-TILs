def n_dec(n):
    if n == 0:
        return

    print(n, end = " ")
    n_dec(n-1)

def n_inc(n):
    if n == 0:
        return

    print(num - n + 1, end = " ")
    n_inc(n-1)

num = int(input())

N = num

n_inc(N)
print()
n_dec(N)