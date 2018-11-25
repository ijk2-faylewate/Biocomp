#NOTE: can generalize to 2 rules for data 1, for an avg of 24, best 25. Settings: Population 50, mutation rate 0.02,
#between 375 and 400 generations

from individual import individual
from individual import child
from random import *
import copy

seed()

#VARS
dataSet = 1
# chromosome length and Population size, and data set

if dataSet == 1:
    chromosomeAmount = 60
else:
    chromosomeAmount = 80

popSize = 50
mutationRate = 0.02

generationLimit = 400

#not to be altered
avgFitness = 0.0
generation = 0
convergence = 0
done = False


# Population lists
population = []
offspring = []

fitCheck = 0

print('Original/initial')
# INITIALISE and EVALUATE
for genes in range(popSize):
    # INITIALISE
    indiv = individual()
    indiv.BinGeneCreateInit(chromosomeAmount)
    # EVALUATE
    #indiv.fitnessCalc()
    population.append(indiv)


fitCheck = 0

best = population[0]
newBest = population[0]

#	REPEAT UNTIL DONE
while generation < generationLimit:
    print('')
    avgFitness = 0.0
    generation = generation + 1
    print('Gen = ',generation)
    #		1 SELECT parents
    # tornement
    #offspring.append(best)
    for x in range(popSize ):
        #offspring.append(best)
        parent1 = randrange(0, popSize)
        parent2 = randrange(0, popSize)

        if population[parent1].fitness >= population[parent2].fitness:
            offspring.append(population[parent1])
        else:
            offspring.append(population[parent2])
        offspring.append(best)
    #offspring.append(best)

    fitCheck = 0

    # 2 RECOMBINE pairs of parents (typically in range (0.6, 0.9)) CURRENTLY NOT 6 TO 9
    print('')
    oneHead = []
    oneTail = []
    twoHead = []
    twoTail = []
    population.clear()

    #print('Crossover')
    halfway = int(popSize / 2)
    crossPointRuleAvoid = int(chromosomeAmount / 10)
    ruleAvoidCount = 0
    for x in range(halfway):
        singlePointCross = randrange(0, chromosomeAmount, crossPointRuleAvoid)

        for i in range(0,singlePointCross):
            oneHead.append(offspring[x].genes[i])
            twoHead.append(offspring[x + halfway].genes[i])

        for i in range(singlePointCross,chromosomeAmount):
            oneTail.append(offspring[x].genes[i])
            twoTail.append(offspring[x + halfway].genes[i])


        child1 = copy.deepcopy(child())
        child2 = copy.deepcopy(child())

        child1.populateChild(oneHead, twoTail)
        child2.populateChild(twoHead, oneTail)

        population.append(child1)
        population.append(child2)

        twoTail.clear()
        oneTail.clear()
        oneHead.clear()
        twoHead.clear()

    fitCheck = 0
    best = population[0]

    #		3 MUTATE the resulting offspring AND 4 EVALUATE
    for x in range(popSize):
        population[x].mutate(mutationRate, chromosomeAmount)
        population[x].conflictRes(chromosomeAmount)
        population[x].fitnessCalc(chromosomeAmount,dataSet)
        #print(population[x].fitness)
        fitCheck = fitCheck + population[x].fitness

        if population[x].fitness > best.fitness:
            best = population[x]

    newBest = population[0]

    print('Best:', best.fitness)



    offspring.clear()
    print('AVG fitness:',fitCheck / popSize)
    avgFitness = fitCheck / popSize



    #print(best.condition)
    #print('Rules matched by best',len(set(best.compareBestWithDataFile(dataSet,wildLimit))))

    # newAvg = 0
    # for x in range(popSize):
    #     newAvg = newAvg + len(set(population[x].compareBestWithDataFile(dataSet,wildLimit)))
    #     if len(set(population[x].compareBestWithDataFile(dataSet,wildLimit))) > len(set(newBest.compareBestWithDataFile(dataSet,wildLimit))):
    #         newBest = population[x]
    #
    # avgRes = newAvg / popSize
    # print('New avg', avgRes )
    # print('New best', len(set(newBest.compareBestWithDataFile(dataSet,wildLimit))))
    #
    # print(newBest.condition)
    # print(newBest.output)
    #print(best.genes)
    print('')
    print(best.conditionsMatched)
    #offspring.append(best)

    if done == False:
        if avgFitness == float(best.fitness):
            convergence = generation
            done = True
    #	DONE
    # END

chrm = int(chromosomeAmount / 10)
for x in range(chromosomeAmount):
    if x % chrm == 0:
        print('')
    print(best.genes[x],end='')


#print('convergence at', convergence, 'generations')