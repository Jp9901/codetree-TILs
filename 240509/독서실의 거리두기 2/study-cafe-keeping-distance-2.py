n = int(input())
li = list(map(int,list(input())))


# sol 1. -------------------

# max_dist = 0
# # 새 한 명이 i번째 자리를 갈 때
# for i in range(n):

#     # 자리가 이미 있을 때
#     if li[i] == 1:
#         continue
    
#     # i번째 자리에 앉을 때
#     li[i] = 1
#     position = [idx for idx, val in enumerate(li) if val==1]
    
#     # 거리 구하기
#     dist = n
#     for j in range(1,len(position)):
#         dist = min(dist, abs(position[j]-position[j-1]))
#     max_dist= max(max_dist,dist)
    
#     # 데이터 리셋
#     li[i] = 0

# sol 2. ----------------

# 자리가 있는 위치
position = [idx for idx, val in enumerate(li) if val==1]

# 최대 위치가 1과 1 사이에 위치할 때
btw_dist = []
for i in range(1, len(position)):
    btw_dist.append(abs(position[i]-position[i-1]))

# 사이 거리가 홀수일 때,
if max(btw_dist)%2 == 0:
    btw_max = max(btw_dist)//2
# 짝수일 때
else: 
    btw_max = (max(btw_dist)-1)//2

# 최대 위치가 마지막에 위치할 때
end_dist = (n-1) - position[-1]

max_dist = max(btw_max, end_dist)
print(max_dist)