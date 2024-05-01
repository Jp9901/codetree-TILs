n = int(input())
li = list(map(int, input().split()))

li.sort()

group_max = 0
for i in range(n):
    # i번째와 2n - 1 - i번째 원소를 매칭합니다.
    group_sum = li[i] + li[2*n - 1 - i]
    if group_sum > group_max:
        # 최댓값을 갱신합니다.
        group_max = group_sum

print(group_max)