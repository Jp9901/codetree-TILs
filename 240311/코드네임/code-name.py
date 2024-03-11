class agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = []
min_score = 100
for i in range(5):
    tmp = input().split()
    name = tmp[0]
    score = int(tmp[1])
    if score <  min_score:
        min_score = score
        min_idx = i
    agents.append(agent(name, score))

print(agents[min_idx].name, agents[min_idx].score, sep = " ")