n,m = map(int,input().split())

pos_A = [0]
pos_B = [0]

# 시간별 A의 위치
for _ in range(n):
    d, t = input().split()
    t = int(t)
    for i in range(1,t+1):
        if d == 'L':
            pos_A.append(pos_A[-1]-1)
        else:
            pos_A.append(pos_A[-1]+1)

# 시간별 B의 위치
for _ in range(m):
    d, t = input().split()
    t= int(t)
    for i in range(1,t+1):
        if d == 'L':       
            pos_B.append(pos_B[-1]-1)
        else:
            pos_B.append(pos_B[-1]+1)


for i in range(1,len(pos_A)):
    if pos_A[i] == pos_B[i]:
        print(i)
        break
else:
    print(-1)