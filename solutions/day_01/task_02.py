def createSortArrays(firstArray, secondArray, fileInput):
    #fileName = input("please enter the file path:\n")
    #fileOpen = open(fileName, "r")
    
    for line in fileInput:
        splittedLine = line.split()
        firstArray.append(int(splittedLine[0]))
        secondArray.append(int(splittedLine[1]))
        
    firstArray.sort()
    secondArray.sort()
    
def solution(fileInput):
    firstArray = [] 
    secondArray = []
    
    createSortArrays(firstArray, secondArray, fileInput)
    
    lastIndexFirstArray = 0
    lastIndexSecondArray = 0
    totalNumberFind = 0
    timeNumberInFirstArray = 1
    similarityScore = 0
    
    arrayLength = range(len(firstArray))
    
    for indexFirstArray in arrayLength:
        if(indexFirstArray < lastIndexFirstArray):
            continue
        for indexSecondArray in arrayLength:
            if(firstArray[indexFirstArray] < secondArray[indexSecondArray]):
                break
            
            if(indexSecondArray < lastIndexSecondArray):
                continue
            
            while(firstArray[indexFirstArray] == secondArray[indexSecondArray+totalNumberFind]):
                totalNumberFind += 1
                
            if(totalNumberFind > 0):
                while(firstArray[indexFirstArray] == firstArray[indexFirstArray + timeNumberInFirstArray]):
                    timeNumberInFirstArray += 1
                lastIndexFirstArray = indexFirstArray + timeNumberInFirstArray
                lastIndexSecondArray = indexSecondArray + totalNumberFind
            
            similarityScore = similarityScore + (firstArray[indexFirstArray] * timeNumberInFirstArray * totalNumberFind)
            
            totalNumberFind = 0
            timeNumberInFirstArray = 1
     
    print(similarityScore)   
    #return similarityScore