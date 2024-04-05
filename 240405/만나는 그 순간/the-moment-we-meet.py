N,M=tuple(map(int,input().split()))

A=[]
B=[]
for _ in range(N):
    s=input()
    a=s.split()[0]
    b=int(s.split()[1])
    c=tuple([a,b])
    A.append(c)

for _ in range(M):
    s=input()
    a=s.split()[0]
    b=int(s.split()[1])
    c=tuple([a,b])
    B.append(c)

A_move=[]
B_move=[]

# A리스트에 대해 반복하면서, 각 튜플에서 만약 오른쪽이라면
# 시간만큰 1씩 더하면서 리스트에 append 
i=0
for direct, time in A:

    if direct=='R':
        for _ in range(time):
            A_move.append(i)
            i+=1

    else: 
        for _ in range(time):
            A_move.append(i)
            i-=1

#################################
i=0
for direct, time in B:

    if direct=='R':
        for _ in range(time):
            B_move.append(i)
            i+=1

    else: 
        for _ in range(time):
            B_move.append(i)
            i-=1

#################################
#print(B_move)

for i in range(1,max(len(A_move),len(B_move))):
    if A_move[i] == B_move[i]:  
        print(i)
        break