def lcm(n,m):
    for i in range(max(n,m),n*m+1):
        if i%n == 0 and i%m == 0:
            print(i)
            break

n,m = map(int,input().split())
lcm(n,m)