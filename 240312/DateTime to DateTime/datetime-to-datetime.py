a,b,c = map(int, input().split())

if a < 11 and b < 11 and c < 11:
    print(-1)
else:
    elapsed_t = (24*60*a + 60*b + c) - (24*60*11 + 60*11 + 11) 

print(elapsed_t)