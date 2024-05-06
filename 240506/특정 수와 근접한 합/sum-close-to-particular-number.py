n,s = map(int, input().split())

li = list(map(int, input().split()))
# print(li)

# S와의 차이가 최소
min_diff = s # 초기값 임의 설정

# 두 개의 수 제외
for i in range(n-1):
    for j in range(i+1,n):
        sum_val = sum(li) - (li[i]+li[j])
        diff = abs(sum_val-s)

        min_diff = min(min_diff,diff)

print(min_diff)