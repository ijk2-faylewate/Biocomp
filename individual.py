from random import*
from ruleStructure import conditionAndOutput
#from ruleStructure import countBits
import dataFromFile
#import data3Tools

seed()
#Lists for test and train
testData = []
trainingData = []

#Data sets
data1 = dataFromFile.data('data1.txt', 6)
data2 = dataFromFile.data('data2.txt', 8)
data3 = dataFromFile.floatData('data3.txt', 8)

#count = 0

#Seperate training and test data in Data3
for x in range(len(data3)):
    if x % 3 == 0:
        testData.append(data3[x])
    else:
        trainingData.append(data3[x])
        #print(count)
        #count = count + 1


#Compare conditions of two rules
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

#Compare output of two rules
def compareOutput(condOutPair, dataToUse):
    result = False
    if condOutPair == dataToUse:
        result = True
    elif condOutPair != dataToUse:
        result = False
    return result

#Create initial individuals
class individual:
    def __init__(self):
        self.genes = []
        self.fitness = 0


    #initialise gene
    def BinGeneCreateInit(self, geneLength):
        condLength = int(geneLength / 10)
        count = 0
        for genes in range(geneLength):

            #Generate random chromosomes
            if count == condLength - 1:
                bin = randrange(0,2)
                count = 0
            elif count < condLength - 1:
                bin = randrange(0,3)
                count = count + 1
            self.genes.append(bin)



    #Calculate fitness from number of chromosomes that == 1. OLD, NO LONGER IN USE
    def fitnessCalc(self):
        for genes in self.genes:
            if genes == 1:
                self.fitness = self.fitness + 1

    #def clearPop(self):
     #   self.genes.clear()

#Post crossover population
class child:
    def __init__(self):
        self.genes = []
        self.fitness = 0
        self.conditionsMatched = []
        self.condition = []
        self.output = []

    #Combine head and tail for child
    def populateChild(self, chrom1Head, chrom2Tail):

        for x in chrom1Head:
            self.genes.append(x)
            #print(chrom1Head[x])
        #print('class',self.genes)

        for x in chrom2Tail:
            self.genes.append(x)




    #Calculate Fitness of individals
    def fitnessCalc(self,chromosomLength, dataSet):


        condOutPair = []
        if dataSet  == 1:
            dataToUse = data1
        elif dataSet == 2:
            dataToUse = data2
        elif dataSet == 3:
            dataToUse = trainingData

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

        #Calculate fitnes by comparison with data set
        for x in range(setLength):
            for j in range(10):
                if compare(condOutPair[j].condition, dataToUse[x].condition, condLength) is True:
                    if compareOutput(condOutPair[j].output,dataToUse[x].output) is True:
                        self.fitness = self.fitness + 1
                        if self.fitness > 17:
                            stop = 'k'
                        self.condition.append(condOutPair[j].condition)
                        self.output.append(dataToUse[x].output)
                    #else:
                     #   continue

                #else:
                    #continue
                    break


    #Mutate genes. Bit flip.
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


    #Calculate percentage of correclty predidcted outputs in test set
    def test(self):
        isMatch = 0
        condOutPair = []
        chromLength = 80
        condLength = int(chromLength / 10)

        # Seperate temporarily into condition/output pairs
        condCount = 0
        for x in self.genes:
            if condCount == chromLength:
                break
            rule = conditionAndOutput()

            rule.collectConditionOutput(condLength, condCount, self.genes)
            condOutPair.append(rule)
            condCount = condCount + condLength


        testLeng = len(testData)
        for y in range(testLeng):
            for x in range(10):
                if compare(condOutPair[x].condition, testData[y].condition, condLength) is True:
                    if compareOutput(condOutPair[x].output, testData[y].output) is True:
                        isMatch = isMatch + 1

                    break
        percentage = (isMatch / testLeng) * 100
        pround = round(percentage, 2)
        #print(pround,'%')

        return pround



