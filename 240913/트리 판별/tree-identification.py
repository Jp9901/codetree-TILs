from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().split()

m = int(data[0])
graph = defaultdict(list)
indegree = defaultdict(int)

if m == 0:
    print(1)
    sys.exit()

nodes = set()

for i in range(1, len(data), 2):
    a = int(data[i])
    b = int(data[i+1])
    graph[a].append(b)
    indegree[b] += 1
    nodes.update([a, b])

root = None
for node in nodes:
    if indegree[node] == 0:
        if root is not None:
            print(0)
            sys.exit()
        root = node

if root is None:
    print(0)
    sys.exit()

visit = set()
q = deque([root])

while q:
    node = q.popleft()
    if node in visit:
        print(0)
        sys.exit()
    visit.add(node)
    for n in graph[node]:
        q.append(n)

if len(visit) == len(nodes):
    print(1)
else:
    print(0)