from individual import individual
from individual import child
from random import *
import copy
import csv

from matplotlib import pyplot as plt

#Lists for plotting
bestPlot = []
avgPlot = []
percentPlot =[]

#Random seed
seed()

#Set chromosome length, specific to data set.
dataSet = 1

#For testing different parameters over epochs
isComp = False

#Select Chromosome length depending on dataset
if dataSet == 1:
    chromosomeAmount = 60
else:
    chromosomeAmount = 80

#Parameters for search
popSize = 100
mutationRate = 0.02
generationLimit = 100

#Loop for epoch, mainly for testing parameters at random.
for x in range(1):
    #VARS
    #not to be altered
    avgFitness = 0.0
    generation = 0
    convergence = 0
    done = False
    fitCheck = 0

    #mutationRate = uniform(0.051, 0.058)
    #popSize = randrange(30,200,2)
    #generationLimit = randrange(50,10000)


    #Population lists
    population = []
    offspring = []

    # INITIALISE and EVALUATE: Random genes for initial population
    for genes in range(popSize):
        # INITIALISE
        indiv = individual()
        indiv.BinGeneCreateInit(chromosomeAmount)
        population.append(indiv)


    #Best gene initialised
    best = population[0]
    newBest = population[0]

    #REPEAT UNTIL DONE - Main loop
    while generation < generationLimit:
        #Reset average fitness, increment generation count
        avgFitness = 0.0
        generation = generation + 1
        print('Gen = ',generation)

        #1 SELECT parents
        # tornement SELECTION. Select parents at random, individual with higher fitness continued. Best individual from
        #previous round automatically included.
        for x in range(popSize):
            offspring.append(best)
            parent1 = randrange(0, popSize)
            parent2 = randrange(0, popSize)

            if population[parent1].fitness >= population[parent2].fitness:
                offspring.append(population[parent1])
            else:
                offspring.append(population[parent2])

        fitCheck = 0

        # 2 RECOMBINE pairs of parents
        #Lists for recombination
        oneHead = []
        oneTail = []
        twoHead = []
        twoTail = []
        #Clear population list
        population.clear()

        #CROSSOVER
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
        #shuffle(population)
        #population.append(best)
        best = population[0]


        #3 MUTATE the resulting offspring, apply conflict resoloution,  and EVALUATE
        for x in range(popSize):
            population[x].mutate(mutationRate, chromosomeAmount)
            population[x].conflictRes(chromosomeAmount)
            population[x].fitnessCalc(chromosomeAmount,dataSet)
            #print(population[x].fitness)
            fitCheck = fitCheck + population[x].fitness
            #Save best individual for next round of selection
            if population[x].fitness > best.fitness:
                best = population[x]

        #best = population[0]
        #display best
        print('Best:', best.fitness)
        bestPlot.append(best.fitness)
        #print(mutationRate,popSize, generationLimit)

        #Clear offspring list for next round
        offspring.clear()
        #Display avg fitness
        print('AVG fitness:',fitCheck / popSize)
        avgPlot.append(fitCheck / popSize)
        avgFitness = fitCheck / popSize

        if dataSet == 3:
            percent = best.test()
            percentPlot.append(percent)
            print('test:', percent, '%')

        #Convergence - NO LONGER USED
        if done == False:
            if avgFitness == float(best.fitness):
                convergence = generation
                done = True
        #	DONE
        # END
    #Testing
    if best.fitness > 52:
        isComp = True
        #print(mutationRate)
        #print(popSize)


#Display most fit gene, divided into rules
chrm = int(chromosomeAmount / 10)
for x in range(chromosomeAmount):
    if x % chrm == 0:
        print('')
    print(best.genes[x],end='')

#Plot Graphs
if dataSet == 3:
    plt.plot(percentPlot, label='test Percent correct')
plt.plot(bestPlot, label='Best')
plt.plot(avgPlot, label='Average')
plt.legend(loc='lower right')
plt.title('Best/Average')
plt.ylabel('Fitness')
plt.xlabel('Generation')
info = 'Data set' + str(dataSet) + ': ' + 'Mutation rate ' + str(mutationRate) + ' Population size ' + str(popSize)
plt.figtext(0,0, info)
plt.show()

fpath = 'data' + str(dataSet) + ' MU' + str(mutationRate) + ' POP' + str(popSize)

# with open(fpath + '.csv', "w", newline='') as f:
#     writeStat = csv.writer(f,delimiter =',')
#     # for x in range(len(bestPlot)):
#     #     f.write(str(bestPlot[x]))
#     #     f.write('\n')
#     # f.write('#')
#     #
#     # for x in range(len(avgPlot)):
#     #     f.write(str(avgPlot[x]))
#     #     f.write('\n')
#     # f.write('#')
#
#     for x in range(len(percentPlot)):
#         f.write(str(percentPlot[x]))
#         f.write(('%'))
#         f.write('\n')
#     f.write('#')

