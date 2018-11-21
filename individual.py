from random import*
from ruleStructure import conditionAndOutput
#from ruleStructure import countBits
import dataFromFile

seed()

#wildCard = False

data1 = dataFromFile.data('data1.txt', 6)
data2 = dataFromFile.data('data2.txt', 8)
data3 = dataFromFile.floatData('data3.txt', 8)

class individual:
    def __init__(self):
        self.genes = []
        self.fitness = 0


    #create Gene
    def BinGeneCreateInit(self, geneLength):
        condLength = int(geneLength / 10)
        count = 0
        for genes in range(geneLength):

            #Generate random chromosomes
            if count == condLength - 1:
                cock = randrange(0,2)
                count = 0
            elif count < condLength - 1:
                cock = randrange(0,3)
                count = count + 1
            self.genes.append(cock)



    #Calculate fitness from number of chromosomes that == 1
    def fitnessCalc(self):
        for genes in self.genes:
            if genes == 1:
                self.fitness = self.fitness + 1

    #def clearPop(self):
     #   self.genes.clear()

class child:
    def __init__(self):
        self.genes = []
        self.fitness = 0
        self.rules = []

    def populateChild(self, chrom1Head, chrom2Tail):

        for x in chrom1Head:
            self.genes.append(x)
            #print(chrom1Head[x])
        #print('class',self.genes)

        for x in chrom2Tail:
            self.genes.append(x)


        #print('fin',self.genes)


    def fitnessCalc(self,chromosomLength, dataSet):
        condOutPair = []

        if dataSet  == 1:
            dataToUse = data1
        elif dataSet == 2:
            dataToUse = data2
        elif dataSet == 3:
            dataToUse = data3

        chromLength = chromosomLength
        condLength = int(chromosomLength / 10)

        #Seperate temporarily into condition/output pairs
        condCount = 0
        for x in self.genes:
            if condCount == chromLength:
                break
            rule = conditionAndOutput()

            rule.collectConditionOutput(condLength,condCount,self.genes)
            condOutPair.append(rule)
            condCount = condCount + condLength
            #print('ou',condOutPair[x].output)

        #Assign fitness based on matched rules from data
        for j in range(len(condOutPair)):
            #print(condOutPair[j].output)
            for i in range(len(dataToUse)):
                #if dataToUse[i].output == condOutPair[j].output and dataToUse[i].condition == condOutPair[j].condition:
                #if countBits(dataToUse[i].condition, condOutPair[j].condition, condLength) == True:
                isMatch = True
                for x in range(condLength - 1):
                    if condOutPair[j].condition[x] == 2:
                        isMatch = True
                        continue
                    elif dataToUse[i].condition[x] != condOutPair[j].condition[x]:
                        isMatch = False
                        break
                    elif dataToUse[i].condition[x] == condOutPair[j].condition[x]:
                        isMatch = True
                        continue
                if condOutPair[j].output == 2:
                    print('Mistake')
                if isMatch == True and dataToUse[i].output == condOutPair[j].output:
                    self.fitness = self.fitness + 1
                    self.rules.append(condOutPair[j].condition)
                    self.rules.append(condOutPair[j].output)
                    break
        #print(set(condOutPair.condition))

        # #CONFLICT RESOLOUTOION
        # check = False
        #
        # #For all genes
        # for genesCount in range(len(self.genes)):
        #     #For all rules
        #      for x in range(len(condOutPair)):
        #          #For genes in the conditions of those rules
        #          for i in range(len(condOutPair[x].condition)):
        #             if self.genes[genesCount] != condOutPair[x].condition[i]:
        #                  check = False
        #                  break
        #             else:
        #                 check = True
        #
        #          if check == True:
        #              if sel.genes

             #       elif i == condLength - 1 and genes != condOutPair[x].output:
              #          genes = 'g'

        #print('c', condOutPair[x].condition,'Out', condOutPair[x].output)



    def mutate(self, mutationRate, chromosomeLength):
        testCount = 0
        condLength = int(chromosomeLength / 10)
        condCount = 0
        for genes in self.genes:
            chance = random()
            chanceForRule = randrange(2,4)

            if chance < mutationRate:
                if chanceForRule % 2 == 0 and condCount != condLength - 1:
                     self.genes[testCount] = 2

                elif genes == 1:
                    self.genes[testCount] = 0
                elif genes == 0:
                    self.genes[testCount] = 1

            testCount = testCount + 1
            condCount = condCount + 1

            if condCount == condLength:
                condCount = 0
                #print('aft',self.genes)


    #Stop conflicting output from same rule by flipping one output
    def conflictRes(self, chromosomeLength):
        condLength = int(chromosomeLength / 10)
        outerCount = 0
        innerCount = 0
        tempCondOne = []
        tempCondTwo = []
        tempOutputOne = None
        tempOutputTwo = None
        #print(self.genes)

        for x in range(condLength + condLength):

            for y in range(condLength + condLength):

                for z in range(condLength):
                    if z < condLength - 1:
                        tempCondOne.append(self.genes[z + outerCount])
                        tempCondTwo.append(self.genes[z + innerCount])
                    elif z == condLength - 1:
                        tempOutputOne = self.genes[z + outerCount]
                        tempOutputTwo = self.genes[z + innerCount]

                if tempCondOne == tempCondTwo and tempOutputOne != tempOutputTwo:
                    if self.genes[z + innerCount] == 1:
                        self.genes[z + innerCount] = 0
                    elif self.genes[z + innerCount] == 0:
                        self.genes[z + innerCount] = 1

                tempCondTwo.clear()
                tempOutputTwo = None
                tempCondOne.clear()
                tempOutputOne = None


                innerCount = innerCount + condLength
                if innerCount == chromosomeLength:
                    break

            outerCount = outerCount + condLength
            innerCount = 0
            if outerCount == chromosomeLength:
                break



        # condLength = int(chromosomeLength / 10)
        # count = 0
        # innerCount = 0
        # outerCount = 0
        #
        # print(self.genes)
        # for out in range(condLength):
        #     #print('o',out)
        #
        #     for x in range(chromosomeLength):
        #         if innerCount == condLength:
        #             innerCount = 0
        #
        #         print(self.genes[x + outerCount], self.genes[innerCount])
        #         if self.genes[x + outerCount] != self.genes[innerCount]:
        #             count = 0
        #             #break
        #         #elif count == condLength - 1: #and self.genes[x] != self.genes[x + condLength]:
        #         #     if self.genes[x + outerCount] != self.genes[innerCount]:
        #         #         print('Mistake')
        #         #         if self.genes[x + outerCount] == 1:
        #         #             self.genes[x + outerCount] = 0
        #         #         elif self.genes[x + outerCount] == 0:
        #         #              self.genes[x + outerCount] = 1
        #         #
        #         #     else:
        #             #break
        #         elif self.genes[x + outerCount] == self.genes[innerCount]:
        #             count = count + 1
        #         innerCount = innerCount + 1
        #
        #     outerCount = outerCount + condLength
        #     innerCount = 0


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


#For every rule in chromosome
    #Compare with every other rule in chromosome
        #if all genes in condition the same
            #if output different
                #flip bit of one output
            #endif
        #else do nothing