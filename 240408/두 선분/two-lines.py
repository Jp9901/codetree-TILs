x1, x2 ,x3, x4=tuple(map(int,input().split()))


if x2>=x3 and x1<= x4:
    print('intersecting')
elif x4>=x1 and x2>=x3:
    print('intersecting')
else:
    print("nonintersecting")