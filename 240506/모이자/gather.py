import sys

# 최댓값의 초기값 지정 => 최솟값 찾을 때 사용
INT_MAX = sys.maxsize

n = int(input())
nums = list(map(int,input().split()))

min_dist = INT_MAX

# 각 i번째 집으로 모였을 때의 합
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j-i) * nums[j]

    min_dist = min(min_dist, sum_dist)

print(min_dist)