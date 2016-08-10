from objects.environment import Environment
from objects.agents import Agent


class Simulator():
    def __init__(self, agentsNumber):
        self.agentsNumber = agentsNumber
        self.agentsList = list()
        for x in range(agentsNumber):
            agent = Agent("agent" + str(x))
            agent.updateFactValue("positionX", 0)
            agent.updateFactValue("positionY", 0)
            self.agentsList.append(agent)
        self.environment = Environment()
        self.environment.setAgents(self.agentsList)

    def initSimulation(self, maxClockStep, motionStrategy=None):
        for x in range(0, maxClockStep, 1):
            for agent in self.agentsList:
                agent.updateFactValue("positionX", x)
                agent.updateFactValue("positionY", x)
                print(agent.getAgentName() + " : " + str(agent.getFactValue("positionX")) + "-" + str(
                    agent.getFactValue("positionY")))
