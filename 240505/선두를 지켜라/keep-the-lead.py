n,m = map(int, input().split())

pos_A = [0]
pos_B = [0]

for _ in range(n):
    v, t = map(int,input().split())
    for _ in range(t):
        pos_A.append(pos_A[-1]+v)

for _ in range(m):
    v, t = map(int,input().split())
    for _ in range(t):
        pos_B.append(pos_B[-1]+v)


# 선두가 바뀐 횟수
# 리더가 A면 1, B면 2
leader, cnt = 0,0
for i in range(1,len(pos_A)):
    if pos_A[i] > pos_B[i]:

        # 기존 리더가 B일 때, 횟수 증가
        if leader == 2:
            cnt += 1
        leader = 1

    elif pos_A[i] < pos_B[i]:

        # 기존 리더가 A일 때, 횟수 증가
        if leader == 1:
            cnt += 1
        leader = 2
print(cnt)