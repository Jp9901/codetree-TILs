def cal(a,b):
    if min(a,b) == a:
        return min(a,b)+10, max(a,b)*2
    else:
        return max(a,b)*2, min(a,b)+10

a,b = map(int, input().split())

print(cal(a,b)[0],cal(a,b)[1], sep=" ")