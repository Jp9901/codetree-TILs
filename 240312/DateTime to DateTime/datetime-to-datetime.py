a,b,c = map(int, input().split())
elapsed_t = (24*60*a + 60*b + c) - (24*60*11 + 60*11 + 11) 

if elapsed_t < 0:
    print(-1)
else:
    print(elapsed_t)