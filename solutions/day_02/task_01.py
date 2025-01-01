import fileinput

def calculateNumberOfSaveLevels():
    fileName = input("please enter the file path:\n")
    fileOpen = open(fileName, "r")
    
    singleLevel = []
    safeReports = 0
    
    for line in fileOpen:
        splittedLine = line.split()
        
        for index in range(len(splittedLine)):
            singleLevel.append(int(splittedLine[index]))
        #print(singleLevel)
        
        if(checkLevelSafeness(singleLevel)):
            safeReports += 1
        singleLevel = []
        
    return safeReports

def checkLevelSafeness(levelToCheck):
    isSafe = True
    isIncreasing = False
    isDecreasing = False
    
    for index in range(len(levelToCheck)-1):
        #print("first element: " + str(levelToCheck[index]))
        #print("second element: " + str(levelToCheck[index+1]))
        difference = levelToCheck[index] - levelToCheck[index+1]
            
        if(difference < -3 or difference > 3 or difference == 0):
            isSafe = False
            break
        
        if(difference < 0 ):
            isIncreasing = True
        else:
            isDecreasing = True
            
        if(isDecreasing & isIncreasing):
            isSafe = False
            break
            
    return isSafe
                  
print(calculateNumberOfSaveLevels())