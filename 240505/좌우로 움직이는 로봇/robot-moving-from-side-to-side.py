n, m = map(int, input().split())

pos_A = [0]
pos_B = [0]

for _ in range(n):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            pos_A.append(pos_A[-1]-1)
        else:
            pos_A.append(pos_A[-1]+1)

for _ in range(m):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            pos_B.append(pos_B[-1]-1)
        else:
            pos_B.append(pos_B[-1]+1)

# 횟수
cnt = 0
time_A = len(pos_A)
time_B = len(pos_B)
min_time = min(time_A,time_B)
max_time = max(time_A,time_B)

# 1~min_time 동안 변한 횟수
for i in range(1,min_time):
    if pos_A[i] == pos_B[i] and pos_A[i-1] != pos_B[i-1]:
        cnt += 1

# min_time ~ max_time 동안 변한 횟수
for i in range(min_time+1, max_time):
    # A가 더 오래동안 움직였을 때
    if time_A > time_B :
        if pos_A[i] == pos_B[min_time-1] and pos_A[i-1] != pos_B[min_time-1]:
            cnt += 1
    # 그 외
    else:
        if pos_A[min_time-1] == pos_B[i] and pos_A[min_time-1] != pos_B[i-1]:
            cnt += 1

print(cnt)