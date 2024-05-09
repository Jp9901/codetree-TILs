n = int(input())

li = [int(input()) for _ in range(n)]

# 모든 위치에 놓여야하는 블럭의 수
target = sum(li)/n

# sol 1.
# # 최댓값인 위치에서 최솟값인 위치로 이동 => 시간초과
# cnt = 0
# while li.count(target) != n:
#     max_idx = li.index(max(li))
#     min_idx = li.index(min(li))
#     li[max_idx] -= 1
#     li[min_idx] += 1
#     cnt += 1

# sol 2.
# 모든 블럭 수를 target으로 맞춰줌
cnt = 0
for i in range(n):
    cnt += abs(li[i]-target)
    li[i] = target

# 블럭의 움직임이 중복되므로 2로 나눔
cnt = int(cnt//2)
print(cnt)