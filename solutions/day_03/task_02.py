import fileinput
import re #regular expression

def sumOfMulWithDoAndDont():
    fileName = input("please enter the file path:\n")
    fileOpen = open(fileName, "r")
    
    # Define the pattern
    do_dont_pattern = r"do\(\)(.*?)(?:don't\(\)|$)"
    
    allMultiplication = []
    totalSum = 0
    
    for line in fileOpen:
        line = "do()" + line
        allMultiplication = re.finditer(r"do\(\)(.*?)(?:don't\(\)|$)", line)
        print("allMultiplication: " + str(allMultiplication))
        for element in allMultiplication:
            totalSum = totalSum + sumOfMul(str(element))
            
    print("totalSum: " + str(totalSum))
    
def sumOfMul(stringWithMul):
    allInnerMultiplication = []
    totalSum = 0
    
    allInnerMultiplication = re.findall(r"mul\(\d{1,3},\d{1,3}\)", stringWithMul)
    print("allInnerMultiplication: " + str(allInnerMultiplication))
    for element in allInnerMultiplication:
        totalSum = totalSum + multiplication(element)
        
    return totalSum

def multiplication(moltiplicationFunction):
    allNumbers = re.findall(r"\d{1,3}", moltiplicationFunction)
    
    firstInt = int(allNumbers[0])
    secondInt = int(allNumbers[1])
    
    print("firstInt: " + str(firstInt))
    print("secondInd: " + str(secondInt))
    
    return firstInt*secondInt
    
sumOfMulWithDoAndDont()