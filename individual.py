from random import*
from ruleStructure import conditionAndOutput
#from ruleStructure import countBits
import dataFromFile

seed()

#wildCard = False

data1 = dataFromFile.data('data1.txt', 6)
data2 = dataFromFile.data('data2.txt', 8)
data3 = dataFromFile.floatData('data3.txt', 8)


#matchedData = []

def compare(condOutPair,dataToUse, condLength):
    match = True
    for r in range(condLength - 1):
        if condOutPair[r] == 2:
            continue
        elif condOutPair[r] == dataToUse[r]:
            continue
        elif condOutPair[r] != dataToUse[r]:
            match = False

    return match

def compareOutput(condOutPair, dataToUse):
    result = False
    if condOutPair == dataToUse:
        result = True
    elif condOutPair != dataToUse:
        result = False
    return result


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
        self.conditionsMatched = []
        self.condition = []
        self.output = []


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
        #print(self.fitness)
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


        setLength = len(dataToUse)


        for x in range(setLength):
            for j in range(10):
                if compare(condOutPair[j].condition, dataToUse[x].condition, condLength) is True:
                    if compareOutput(condOutPair[j].output,dataToUse[x].output) is True:
                        self.fitness = self.fitness + 1
                    else:
                        continue

                break








        #             if condOutPair[i].output == dataToUse[x].output:
        #                 self.fitness = self.fitness + 1
        #                 self.conditionsMatched.append(condOutPair[i].condition)
        #                 self.conditionsMatched.append(condOutPair[i].output)
        #             else:
        #                 break

        #Assign fitness based on matched rules from data
        #Check rule against dataset, if match go to next rule, restart from begining of dataset

        # for j in range(10):
        #     for i in range(len(dataToUse)):
        #         isMatch = True
        #         twoCount = 0
        #         if self.fitness >= 15:
        #             piss = 'y'
        #         for x in range(condLength - 1):
        #             if condOutPair[j].condition[x] == 2:
        #                 #twoCount = twoCount + 1
        #                 #isMatch = True
        #                 continue
        #             elif dataToUse[i].condition[x] != condOutPair[j].condition[x]:
        #                 isMatch = False
        #                 #break
        #             elif dataToUse[i].condition[x] == condOutPair[j].condition[x]:
        #                 #isMatch = True
        #                 continue
        #             # if condOutPair[j].output == 2:
        #             #     print('Mistake')
        #         if isMatch == True and dataToUse[i].output == condOutPair[j].output:# and twoCount <=4:
        #             self.fitness = self.fitness + 1
        #             self.conditionsMatched.append(dataToUse[i].condition)
        #             self.condition.append(condOutPair[j].condition)
        #             self.output.append(condOutPair[j].output)
        #         break




        #print(len(self.conditionsMatched))

        #print(self.fitness)
        #print(len((self.conditionsMatched)))

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


    def compareBestWithDataFile(self, dataSet, wildlimit):
        if dataSet  == 1:
         dataToUse = data1
        elif dataSet == 2:
         dataToUse = data2
        elif dataSet == 3:
         dataToUse = data3

        returnData = []
        if self.fitness > 15:
            pass
            #print('')
        for j in range(len(dataToUse)):
            for x in range(len(self.condition)):
                match = True
                twoCount = 0
                for z in range(len(dataToUse[j].condition)):

                    if self.condition[x][z] == 2:
                        twoCount = twoCount + 1
                        #match = True
                        continue
                    elif self.condition[x][z] != dataToUse[j].condition[z]:
                        match = False
                        #break
                    elif self.condition[x][z] == dataToUse[j].condition[z]: # and self.output[x] == dataToUse[j].output:
                        #match = True
                        continue

                if match == True: #and twoCount <= wildlimit:
                    #print('self', self.condition[x])
                    #self.fitness = self.fitness + 1
                    returnData.append(dataToUse[j])
                break


        return returnData