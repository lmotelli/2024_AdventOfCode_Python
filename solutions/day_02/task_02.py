import fileinput

def calculateNumberOfSaveLevelsWithProblemDampener():
    fileName = input("please enter the file path:\n")
    fileOpen = open(fileName, "r")
    
    singleLevel = []
    safeReports = 0
    correctedLines = []
    numLine = 0
    
    for line in fileOpen:
        numLine += 1
        splittedLine = line.split()
        
        for index in range(len(splittedLine)):
            singleLevel.append(int(splittedLine[index]))
        
        if(checkLevelSafenessSubArray(singleLevel)):
            safeReports += 1
            correctedLines.append(numLine)
        singleLevel = []
    
    #print("corrected lines:")
    print(correctedLines)
    return safeReports

def checkLevelSafenessSubArray(totalArray):
    if(checkLevelSafeness(totalArray)):
        return True
    
    subArray = []
    
    for index in range(len(totalArray)):
        subArray = copy(totalArray)
        subArray.pop(index)
        
        if(checkLevelSafeness(subArray)):
            return True
        
def copy(totalArray):
    arrayToReturn = []
    for index in range(len(totalArray)):
        arrayToReturn.append(totalArray[index])
        
    return arrayToReturn
        

def checkLevelSafeness(levelToCheck):
    isIncreasing = False
    isDecreasing = False
    
    for index in range(len(levelToCheck)-1):
        difference = levelToCheck[index] - levelToCheck[index+1]
            
        if(difference < -3 or difference > 3 or difference == 0):
            return False
        
        if(difference < 0 ):
            isIncreasing = True
        else:
            isDecreasing = True
            
        if(isDecreasing & isIncreasing):
            return False
            
    return True

print(calculateNumberOfSaveLevelsWithProblemDampener())