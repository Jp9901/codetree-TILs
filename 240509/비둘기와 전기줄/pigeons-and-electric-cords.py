n = int(input())

info = [list(map(int,input().split())) for _ in range(n)]

# 비둘기 위치(처음 위치를 모르므로 -1)
position = [-1]*11

cnt = 0
for i,p in info:

    # 비둘기 위치를 모를 때,
    if position[i] == -1:
        position[i] = p
        
    # 비둘기 위치를 알 때,
    else:
        # 자리가 동일할 때,
        if position[i] == p:
            continue
        # 자리가 동일하지 않을 때,
        else:
            position[i] = p
            cnt += 1

print(cnt)