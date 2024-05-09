n = int(input())

li = [int(input()) for _ in range(n)]

# 모든 위치에 놓여야하는 블럭의 수
target = sum(li)/n

# 최댓값인 위치에서 최솟값인 위치로 이동
cnt = 0
while li.count(target) != n:
    max_idx = li.index(max(li))
    min_idx = li.index(min(li))
    li[max_idx] -= 1
    li[min_idx] += 1
    cnt += 1

print(cnt)