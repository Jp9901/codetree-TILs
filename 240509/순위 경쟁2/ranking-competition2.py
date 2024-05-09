n = int(input())
info =[]
A,B = 0,0

for _ in range(n):
    c, s = input().split()
    s = int(s)
    info.append([c,s])

# 변경 횟수
cnt = 0
leader = 'AB'
for c,s in info:
    if c =='A':
        A += s
    else:
        B += s

    if A > B:
        if leader != 'A':
            leader ='A'
            cnt += 1
    elif A < B:
        if leader != 'B':
            leader = 'B'
            cnt += 1
    else:
        if leader != 'AB':
            leader='AB'
            cnt += 1

print(cnt)