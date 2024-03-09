def sum_val(n):
    if n == 0:
        return 0

    return n + sum_val(n-1)

N = int(input())
print(sum_val(N))