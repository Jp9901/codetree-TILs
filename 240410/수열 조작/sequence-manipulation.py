from collections import deque



N=int(input())
q=deque()
for i in range(N):
    q.append(i+1)






while len(q)>1:
    
    q.popleft()
    a=q[0]
    q.popleft()
    q.append(a)


print(q[0])