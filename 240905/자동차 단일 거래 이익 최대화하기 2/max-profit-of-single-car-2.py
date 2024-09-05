#내림차순정렬이면  0출력
# 3 100 2 10
# 99 100 3 10

#최대값을 기준으로 왼쪽의 최소값과 이득 계산
#그리고 위의 최대값 기준으로 오른쪽에서 다시 최대값 계산 

# n=int(input())
# prices=list(map(int,input().split()))
# price=prices.copy()
# sp=sorted(price, reverse=True)

# ans=0
# i=0

# if sp==price:
#     print(0)

# else:
#     while price!=[]:   
#         i=price.index(max(price))
#         small_p=price[:i]
#         ans=max(max(price)-min(small_p),ans)
#         price=price[i+1:]
    
#     print(ans)
########################################################
# n = int(input())
# prices = list(map(int, input().split()))

# # 최소값과 최대 차이 초기화
# min_price = float('inf')
# max_diff = 0

# # 리스트를 한 번만 순회하면서 계산
# for price in prices:
#     if price < min_price:
#         min_price = price  # 최소값 갱신
#     current_diff = price - min_price  # 현재 값과 최소값의 차이 계산
#     if current_diff > max_diff:
#         max_diff = current_diff  # 최대 차이 갱신

# print(max_diff)
########################################################

n = int(input())
prices = list(map(int, input().split()))

# 최소값과 최대 차이 초기화
min_price = float('inf')
max_diff = 0

# 리스트를 한 번만 순회하면서 계산
for price in prices:
    
    min_price = min(min_price,price)  # 최소값 갱신
    current_diff = price - min_price  # 현재 값과 최소값의 차이 계산
    
    max_diff=max(max_diff,current_diff)

print(max_diff)