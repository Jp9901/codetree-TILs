A,B,x,y = map(int,input().split())

# 텔러포트 사용 했을 때의 최단 거리
tele_dist = min(abs(A-x)+abs(B-y),abs(A-y)+abs(B-x))

# 텔레포트 사용하지 않았을 때의 최단 거리
dir_dist = abs(B-A)

# 최단 거리
min_dist = min(tele_dist,dir_dist)
print(min_dist)