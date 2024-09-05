n=int(input())
prices=list(map(int,input().split()))
price=prices.copy()
sp=sorted(price, reverse=True)

ans=0
i=0

# if sp==price:
#     print(0)

# else:
while len(price)!=0:   
        i=price.index(max(price))
        small_p=price[:i]
        ans=max(max(price)-min(small_p),ans)
        price=price[i+1:]
    
print(ans)