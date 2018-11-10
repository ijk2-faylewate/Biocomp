#from typing import Any, Union

from individual import individual
from individual import child
from random import *
import copy

seed()
dataSet = 1
# chromosome length and Population size, and data set

if dataSet == 1:
    chromosomeAmount = 60
else:
    chromosomeAmount = 80

popSize = 50
mutationRate = 0.01

generationLimit = 50

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

# Fitness Check
#for candidates in population:
    #fitCheck = fitCheck + candidates.fitness
    #print(candidates.genes)
    # print(candidates.fitness)

#print('AVG fitness: ', fitCheck / popSize)
fitCheck = 0

best = population[0]

#	REPEAT UNTIL DONE
while generation < generationLimit:
    avgFitness = 0.0
    generation = generation + 1
    print('Gen = ',generation)
    #		1 SELECT parents
    # tornement
    for x in range(popSize):
        parent1 = randrange(0, popSize)
        parent2 = randrange(0, popSize)

        if population[parent1].fitness >= population[parent2].fitness:
            offspring.append(population[parent1])
        else:
            offspring.append(population[parent2])

   #
    # Fitness Check
    count = 0
    fitCheck = 0
    #for candidates in offspring:
     #   count = count + 1
        #fitCheck = fitCheck + candidates.fitness
        #print(count,': ',candidates.genes)
        # print(candidates.fitness)

    #print('fitCheck: ', fitCheck)
    #print('AVG fitness:', fitCheck / popSize)
    fitCheck = 0

    # 2 RECOMBINE pairs of parents (typically in range (0.6, 0.9)) CURRENTLY NOT 6 TO 9

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


        child1 = child()
        child2 = child()

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
        population[x].mutate(mutationRate)
        population[x].fitnessCalc(chromosomeAmount,dataSet)
        #print(population[x].fitness)
        fitCheck = fitCheck + population[x].fitness

        if population[x].fitness > best.fitness:
            best = population[x]

    print('Best:', best.fitness)

    offspring.clear()
    print('AVG fitness:',fitCheck / popSize)
    avgFitness = fitCheck / popSize

    print('')

    if done == False:
        if avgFitness == float(best.fitness):
            convergence = generation
            done = True
    #	DONE
    # END
print('convergence at', convergence, 'generations')