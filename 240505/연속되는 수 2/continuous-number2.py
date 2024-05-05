n = int(input())

li = list(int(input()) for _ in range(n))

# 각 동일 수 횟수와 최댓값
cnt = 1
max_cnt = cnt
for i in range(1,n):
    
    # 이전 숫자와 현재 숫자 비교
    if li[i-1] == li[i]:
        cnt += 1

        # 최댓값 갱신
        if cnt > max_cnt:
            max_cnt = cnt

    else:
        cnt = 1

print(max_cnt)