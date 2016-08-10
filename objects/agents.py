class Agent():
    def __init__(self,name = None, facts = None ):
        if name:
            self.name= name;
        else:
            self.name = ''

        if facts:
            self.facts = facts
        else:
            self.facts = dict()

    def getFactValue(self, factName):

        if len(self.facts.keys())>0:
            return self.facts[factName]

    def getFacts(self):
        return self.facts

    def updateFactValue(self,factName,factValue):
        self.facts[factName] = factValue
        print("")

    def getAgentName(self):
        return self.name



