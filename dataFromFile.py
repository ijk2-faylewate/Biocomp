from ruleStructure import conditionAndOutputFromFile
def data(datafile, condLength):
    returnData = []
    f = open(datafile, 'r')
    dFromFile = f.read()
    f.close()
    rule = conditionAndOutputFromFile()

    condCount = 0
    for x in dFromFile:
        if x != '\n' and x != ' ' and condCount != condLength - 1:
            rule.condition.append(int(x))
            condCount = condCount + 1
        elif x == ' ':
            continue
        elif condCount == condLength - 1:
            rule.output = int(x)
            condCount = condCount + 1

        elif x == '\n':
            returnData.append(rule)
            rule = conditionAndOutputFromFile()
            condCount = 0

    return returnData

def floatData(datafile, condLength):
    returnData = []
    f = open(datafile, 'r')
    dFromFile = []
    #dFromFile = f.read()
    for y in f.readlines():
        dFromFile.append(y.strip('\n').split(' '))
    f.close()

    rule = conditionAndOutputFromFile()

    #condCount = 0
    for x in range(len(dFromFile)):
        for y in range(condLength):
            if y < condLength - 1:
                rule.condition.append(dFromFile[x][y])
            else:
                rule.output = dFromFile[x][y]

        returnData.append(rule)
        rule = conditionAndOutputFromFile()

    return returnData





#x = data('data1.txt', 6)
#z = floatData('data3.txt',8)

#for w in z:
#    print(w.condition,w.output)
