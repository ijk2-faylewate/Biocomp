from ruleStructure import conditionAndOutputFromFile

data3Threshold = 0.5

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
                if float(dFromFile[x][y]) >= data3Threshold:
                    rule.condition.append(1)
                elif float(dFromFile[x][y]) < data3Threshold:
                    rule.condition.append(0)
            else:
                rule.output = int(dFromFile[x][y])

        returnData.append(rule)
        rule = conditionAndOutputFromFile()

    return returnData



