def find_parents(n, connections):
    # 부모 노드를 저장할 리스트 초기화 (노드 번호가 1부터 시작하므로 n+1 크기로 설정)
    parent = [0] * (n + 1)
    
    # 연결 정보를 통해 부모-자식 관계 설정
    for a, b in connections:
        # a가 b의 부모 노드라고 가정 (문제에서 주어진 구조를 따라)
        if parent[b] == 0:  # 아직 부모 노드가 설정되지 않은 경우
            parent[b] = a
        else:  # b가 a의 부모인 경우 (양방향이 아님을 가정하면 필요 없는 조건)
            parent[a] = b
    
    # 결과 출력 (2번 노드부터 n번 노드까지의 부모 노드)
    for i in range(2, n+1):
        print(parent[i])

# 입력 받기
n = int(input())  # 노드의 개수
connections = []

for _ in range(n-1):
    a, b = map(int, input().split())
    connections.append((a, b))

# 부모 노드 찾기 및 출력
find_parents(n, connections)