n = int(input())

time = [list(map(int,input().split())) for _ in range(n)]

max_time = 0

for i in range(n):
    run_time = [0]*1000
    for j in range(n):

        # i번째 사람을 해고했을 때,
        if i == j:
            continue

        # 운행되고 있는 시간 = 1
        start, end = time[j]

        run_time[start:end] = [1]*(end-start)
        cnt = run_time.count(1)

        max_time = max(cnt, max_time)

print(max_time)