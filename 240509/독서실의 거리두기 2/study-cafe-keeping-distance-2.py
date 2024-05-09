n = int(input())
li = list(map(int,list(input())))

max_dist = 0
# 새 한 명이 i번째 자리를 갈 때
for i in range(n):

    # 자리가 이미 있을 때
    if li[i] == 1:
        continue
    
    # i번째 자리에 앉을 때
    li[i] = 1
    position = [idx for idx, val in enumerate(li) if val==1]
    
    # 거리 구하기
    dist = n
    for j in range(1,len(position)):
        dist = min(dist, position[j]-position[j-1])
    max_dist= max(max_dist,dist)
    
    # 데이터 리셋
    li[i] = 0

    

print(max_dist)