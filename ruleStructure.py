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


# c = [1,2,3,4,5,6,7,8,9,10,11,12]
# d = [1,2,3,4,5,6,7,8,9,10,11,12]
#
# innercount = 0
# outtercount = 0
# length = len(c)
# faze = 3
# fazeOut = 6
# #Needs two fazes
# for x in range(length):
#
#     if innercount == faze:
#         innercount = 0
#
#     if outtercount == fazeOut:
#         outtercount = 0
#
#     print(c[innercount], d[x])
#     if d[x] % c[innercount] == 0:
#         print('Clck')
#
#     innercount = innercount + 1
#     outtercount = outtercount + 1