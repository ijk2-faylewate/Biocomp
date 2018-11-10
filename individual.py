from random import*
from ruleStructure import conditionAndOutput
import dataFromFile

seed()

wildCard = False

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
                print(count, cock)
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

        condCount = 0
        for x in self.genes:
            if condCount == chromLength:
                break
            rule = conditionAndOutput()

            rule.collectConditionOutput(condLength,condCount,self.genes)
            condOutPair.append(rule)
            condCount = condCount + condLength
            #print('ou',condOutPair[x].output)

        for j in range(len(condOutPair)):
            print(condOutPair[j].output)
            for i in range(len(dataToUse)):
                if dataToUse[i].output == condOutPair[j].output and dataToUse[i].condition == condOutPair[j].condition:
                    self.fitness = self.fitness + 1
                    break

        #print('c', condOutPair[x].condition,'Out', condOutPair[x].output)



    def mutate(self, mutationRate):
        testCount = 0
        for genes in self.genes:
            chance = random()
            if chance < mutationRate:
                #print('bef',self.genes)
                if genes == 1:
                    self.genes[testCount] = 0
                elif genes == 0:
                    self.genes[testCount] = 1

            testCount = testCount + 1
                #print('aft',self.genes)


#for x in range(20):
#    cook = randrange(0, 20, 6)
#    print(cook)