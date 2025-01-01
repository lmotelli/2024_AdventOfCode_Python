import fileinput
import re #regular expression

def sumOfMul():
    fileName = input("please enter the file path:\n")
    fileOpen = open(fileName, "r")
    
    allMultiplication = []
    totalSum = 0
    
    for line in fileOpen:
        allMultiplication = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        #print(allMultiplication)
        for element in allMultiplication:
            totalSum = totalSum + multiplication(element)
            print("totalSum: " + str(totalSum))
    print("final totalSum: " + str(totalSum))
        
        
def multiplication(moltiplicationFunction):
    allNumbers = re.findall(r"\d{1,3}", moltiplicationFunction)
    #print("firstInt: " + str(allNumbers))
    firstInt = int(allNumbers[0])
    secondInt = int(allNumbers[1])
    
    #print("firstInt: " + str(firstInt))
    #print("secondInt: " + str(secondInt))
    return firstInt*secondInt
    
sumOfMul()