n = int(input())

min_r,max_r = 100,0
min_c,max_c = 100,0



for _ in range(n):
    r,c = map(int,input().split())
    min_r = min(min_r,r)
    max_r = max(max_r,r)
    min_c = min(min_c,c)
    max_c = max(max_c,c)
    
length = ((max_r-min_r+1) + (max_c-min_c+1))*2

print(length)