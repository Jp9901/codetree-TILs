n = int(input())

# 위치와 알파벳 정보
value = [0] * 101

for _ in range(n):
    x, info = input().split()
    x = int(x)

    value[x] = 1 if info == 'G' else 2

# 사진의 크기
max_dist = 0

for i in range(101):
    for j in range(i+1, 101):
        cnt_G=0
        cnt_H=0

        # 사람이 존재하면
        if value[i] != 0 and value[j] != 0:
            for k in range(i, j+1):
                if value[k] == 1:
                    cnt_G += 1
                if value[k] == 2:
                    cnt_H += 1

            if cnt_G == 0 or cnt_H == 0 or cnt_G==cnt_H:
                dist = j-i
                max_dist = max(max_dist,dist)

print(max_dist)