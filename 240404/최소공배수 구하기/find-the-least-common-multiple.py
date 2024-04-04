n, m = tuple(map(int, input().split()))


def solution(n,m):
    k= min(n,m)
    l= max(n,m)
    i=1
    while True:
        if (k*i)%l==0:

            print(k*i)
            break

        else:
            i+=1



solution(n,m)