class conditionAndOutput:
    def __init__(self):
        self.condition = []
        self.output = None

    chromCount = 0
    def collectConditionOutput(self, condLength,condCount, chromosome):

        for x in range(condLength):
            if x < condLength - 1:
                self.condition.append(chromosome[x + condCount])
            elif x == condLength - 1:
                self.output = chromosome[x + condCount]



class conditionAndOutputFromFile(conditionAndOutput):
    pass


