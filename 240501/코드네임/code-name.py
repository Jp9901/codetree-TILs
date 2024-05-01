class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# 사람 정보를 담을 리스트
agents = list()

# 가장 낮은 점수
min_val = 100



for i in range(5):
    name, score = input().split()
    score = int(score)
    agents.append(Agent(name,score))
    
    if agents[i].score < min_val:
        min_val = agents[i].score
        min_agent = agents[i].name

print(min_agent, min_val)