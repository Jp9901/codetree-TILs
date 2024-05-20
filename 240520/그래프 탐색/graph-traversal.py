n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

root_vertex = 1
visited = [False]*(n+1)
cnt = 0

def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)


visited[root_vertex] = True
dfs(root_vertex)

print(cnt)