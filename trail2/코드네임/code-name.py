class Agent:
    def __init__(self, code="", score=0):
        self.code = code
        self.score = score

agents = []
for _ in range(5):
    code, score = tuple(input().split())
    agents.append(Agent(code, int(score)))

agents.sort(key=lambda agent: agent.score)
print(f"{agents[0].code} {agents[0].score}")

