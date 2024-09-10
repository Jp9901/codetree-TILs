# 트리의 현재 상태를 어떻게 저장할까?
#각 노드의 부모자식관계, 각 노드의 색상, 트리에 존재하는 노드, 각 노드의 최대 깊이
#노드 추가, 색깔변경, 색깔조회, 점수조회 기능

#100 id 부모 색상 깊이

#추가할수 있는 조건: 기존 노드들의 최대 깊이 고려

#여러개의 트리가 만들어질 수 있다

#각 노드 색상과 깊이를 딕셔너리로 저장하자
#각 노드의 부모를 uf리스트에 저장한다
#색상변경을 위해 x를 부모로 하는 모든 노드를 구하는 함수가 필요하다
#점수 계산을 위해서도 위함수가 필요하다 
colors={}
depths={}
uf=[0]*100000
nodes=set()   #모든 노드 저장


#x의 모든 부모 경로 집합을 계산하는 함수
def find_mother(x):
    m=set()
    m.add(x)
    node=x
    while uf[node]!=node:
        m.add(node)
        node=uf[node]
    m.add(node)
    return m

#x의 자식을 모두 찾는 함수
def find_child(x):

    child=set()
    child.add(x)
    for node in nodes:
        mother=find_mother(node)
        if x in mother:
            child.add(node)
    
    return child

#모든 x 서브트리의 색깔변경 함수
def change_color(x,color):
    childs=find_child(x)
    for child in childs:
        colors[child]=color


#색깔 조회 및 출력함수
def what_color(i):
    print(colors[i])

#점수 출력함수
def score():
    s=0
    for node in nodes:
        c=set()
        childs=find_child(node)
        for child in childs:
            c.add(colors[child])
        s+=(len(c))**2
    print(s)

#깊이 확인 함수 (자식을 낳기 직전인 노드 입력)
def check_d(m):
    count=2
    node=m
    ch=set()
    

    if depths[node]<2:
        return False

    while uf[node]!=node and (node not in ch):
        count+=1
        node=uf[node]
        ch.add(node)
        if depths[node]<count:
            return False

    return True

    
#노드 추가 함수
def create(m_id,p_id,color,max_depth):

    if p_id==-1:
        uf[m_id]=m_id

        nodes.add(m_id)
        depths[m_id]=max_depth
        colors[m_id]=color

    elif check_d(p_id):
        uf[m_id]=p_id

        nodes.add(m_id)
        depths[m_id]=max_depth
        colors[m_id]=color

    
n=int(input())
for _ in range(n):
    order=tuple(map(int,input().split()))

    if order[0]==100:
        j,m_id,p_id,color,max_depth=order
        create(m_id,p_id,color,max_depth)

    elif order[0]==200:
        j,m_id,color=order
        change_color(m_id,color)

    elif order[0]==300:
        j,m_id=order
        what_color(m_id)

    else:
        score()