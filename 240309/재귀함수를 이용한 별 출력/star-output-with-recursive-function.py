def n_star(n):
    if n == 0:
        return

    n_star(n-1)
    print("*"*n)

n = int(input())

n_star(n)