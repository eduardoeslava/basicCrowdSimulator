class Environment:
    def __init__(self, size=None):
        if size:
            self.size = size

    def setAgents(self,agents):
        self.agents = agents

