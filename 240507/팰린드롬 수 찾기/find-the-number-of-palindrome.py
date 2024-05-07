x, y = map(int,input().split())

cnt = 0 
for i in range(x,y+1):
    li = list(map(int,list(str(i))))
    li_rev = list(reversed(li))

    if li == li_rev:
        cnt += 1

print(cnt)