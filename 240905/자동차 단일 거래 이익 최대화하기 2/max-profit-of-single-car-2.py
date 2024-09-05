#내림차순정렬이면  0출력
# 3 100 2 10
# 99 100 3 10

#최대값을 기준으로 왼쪽의 최소값과 이득 계산
#그리고 위의 최대값 기준으로 오른쪽에서 다시 최대값 계산 

n=int(input())
prices=list(map(int,input().split()))
price=prices.copy()
sp=sorted(price, reverse=True)

ans=0
i=0

if sp==price:
    print(0)

else:
    while sum(price)!=0:   ####
        i=price.index(max(price))
        small_p=price[:i]
        ans=max(max(price)-min(small_p),ans)
        price=price[i+1:]
    
print(ans)