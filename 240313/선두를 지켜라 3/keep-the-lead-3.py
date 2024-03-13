N, M = map(int, input().split())

arr_A = [
    list(map(int,input().split())) for _ in range(N)
]

arr_B = [
    list(map(int,input().split())) for _ in range(M)
]

total_time = 0
for i in range(N):
    total_time += arr_A[i][1]

rank = [1,1]
cnt = 0

pos_A = [0 for _ in range(total_time+1)]
pos_B = [0 for _ in range(total_time+1)]

now = 1
for v, t in arr_A:
    for time in range(now,now+t):
        pos_A[time] = v+pos_A[time-1]
    now += t


now = 1
for v, t in arr_B:
    for time in range(now,now+t):
        pos_B[time] = v+pos_B[time-1]
    now += t

cnt = 0
for t in range(total_time):
    if pos_A[t] > pos_B[t]:
        if rank != [1,2]:
            cnt += 1
        rank = [1,2]
    elif pos_A[t] == pos_B[t]:
        if rank != [1,1]:
            cnt += 1
        rank = [1,1]
    else:
        if rank != [2,1]:
            cnt += 1
        rank = [2,1]
print(cnt)