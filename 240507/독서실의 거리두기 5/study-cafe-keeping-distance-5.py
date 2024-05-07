n = int(input())

li = list(map(int,list(input())))


max_dist = 0

# 앉을 자리 찾기
for i in range(n):
    
    # 이미 자리가 있을 때
    if li[i] == 0:
        li[i] = 1

        # 거리 계산
        dist = n
        for j in range(n):
            for k in range(j+1,n):
                if li[j] == 1 and li[k] == 1:
                    dist = min(dist, k-j)

        # 원위치
        li[i] = 0

        max_dist = max(dist, max_dist)

print(max_dist)