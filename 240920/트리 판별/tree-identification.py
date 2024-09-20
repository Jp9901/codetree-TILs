m=int(input())

init=[0]*10009
visit=[False]*10009
graph=[[] for _ in range(10009)]          #모든 간선 기록 (b->a)

nodes=set()      #모든 노드 집합
end=set()        #모든 도착 노드 집합

for _ in range(m):
    a,b=tuple(map(int,input().split()))
    graph[a].append(b)

    nodes.add(a)
    nodes.add(b)
    end.add(b)

    init[b]+=1

check=True

#루트노드를 찾고, 루트노드가 없거나 한개가 아니면 False

roots=list(nodes-end)

if len(roots)!=1:
    check=False
root=roots[0]

nomal_nodes=nodes-set([root])
nomal_nodes=list(nomal_nodes)
for n in nomal_nodes:
    if init[n]!=1:
        check=False


#모든 노드에 대해서 dfs를 실시하여 루트노드에 도달할수있음을 확인

def dfs(x):
    for y in graph[x]:
        # 이미 방문한 노드는 스킵합니다.
        if visit[y]: 
            continue

        visit[y] = True  
        dfs(y)

    return
        
def check_tree():
    dfs(root)
    for n in nomal_nodes:
        if visit[n]==False:
            return False
    return True


# 결과 출력
if check==False:
    print(0)

else:
    check=check_tree()
    if check==False:
        print(0)
    else:
        print(1)