x1,x2,x3,x4 = map(int,input().split())

li = [0] * 101

li[x1:(x2+1)] = [1]*(x2+1-x1)

inter = False

for i in range(x3,x4+1):
    if li[i] == 1:
        inter = True
        break

if inter:
    print('intersecting')
else:
    print('nonintersecting')