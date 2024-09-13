#들어오는 간선이 없는 노드가 단 한개인것을 확인해서 루트노드를 찾는다
# 루트노드에서 bfs를 실시한다 

m=int(input())

from collections import deque

graph=[[] for _ in range(10000)]

nodes=set()
end=set()

for _ in range(m):
    a,b=tuple(map(int,input().split()))
    graph[a].append(b)
    nodes.add(a)
    nodes.add(b)
    end.add(b)


roots=nodes-end
root=list(roots)[0]


def bfs(graph):
    visit=[False]*10000
    visit[root]=True

    q=deque()
    q.append(root)

    while q:
        node=q.popleft()
        nei=graph[node]
        for n in nei:
            if visit[n]==False:
                q.append(n)
                visit[n]=True

    if sum(visit)==len(nodes):
        return 1

    else: 
        return 0
        

if len(roots)!=1:
    print(0)
else:
    print(bfs(graph))