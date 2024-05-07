x,y = map(int,input().split())

max_val = 0
for i in range(x,y+1):
    li = list(map(int,list(str(i))))
    sum_val = sum(li) 

    max_val = max(max_val,sum_val)

print(max_val)