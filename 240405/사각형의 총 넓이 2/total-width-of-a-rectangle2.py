n=int(input())

rects=[tuple(map(int, input().split())) for _ in range(n)]


check=[[0]*200 for _ in range(200)]

for x1,y1,x2,y2 in rects:
    x1,y1=x1+100,y1+100
    x2,y2=x2+100,y2+100


    for x in range(x1,x2):
        for y in range(y1,y2):
            check[x][y]=1 



k=0

for x in range(200):
    for y in range(200):
        if check[x][y]==1:
            k+=1


print(k)