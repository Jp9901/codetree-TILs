m = int(input())

# 그래프 초기화 및 노드 정보
graph = {}
indegree = {}
nodes = set()

for _ in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if a not in indegree:
        indegree[a] = 0
    if b not in indegree:
        indegree[b] = 0
    graph[a].append(b)
    indegree[b] += 1
    nodes.update([a, b])

# 루트 노드 찾기
root = None
for node in nodes:
    if indegree[node] == 0:
        if root is not None:  # 두 번째 루트 발견 시 바로 0 출력
            print(0)
            exit()
        root = node

if root is None:  # 루트 노드가 없는 경우도 트리가 아님
    print(0)
    exit()

# BFS 실행하여 모든 노드 방문 확인
visit = set()
queue = [root]

while queue:
    current = queue.pop(0)
    if current in visit:
        continue
    visit.add(current)
    if current in graph:
        for neighbor in graph[current]:
            queue.append(neighbor)

# 방문한 노드 수와 총 노드 수 비교
if len(visit) == len(nodes):
    print(1)
else:
    print(0)