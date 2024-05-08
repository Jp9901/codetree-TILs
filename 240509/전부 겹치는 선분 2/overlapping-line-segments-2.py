n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]

inter = False

# i번째 선분 제거
for i in range(n):
    x_li = [0]*101
    for j in range(n):

        if i == j:
            continue

        x1, x2 = li[j]
        for k in range(x1,x2+1):
            x_li[k] += 1

        

    if x_li.count(n-1) > 0:
        inter = True
        break

if inter:
    print('Yes')
else:
    print('No')