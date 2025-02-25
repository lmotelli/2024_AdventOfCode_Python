import fileinput
import re #regular expression

def solution(fileInput):
    #fileName = input("please enter the file path:\n")
    #fileOpen = open(fileName, "r")
    
    # Define the pattern
    #do_dont_pattern = r"do\(\)(.*?)(?:don't\(\)|$)"
    
    stringsWithoutDoAndDont = []
    totalSum = 0
    
    for line in fileInput:
        #line = "do()" + line
        stringsWithoutDoAndDont = re.findall(r"^(.*?)don't\(\)|do\(\)(.*?)(?:don't\(\)|$)", line)
        #print("stringsWithoutDoAndDont: " + str(stringsWithoutDoAndDont))
        allMultiplication = re.findall(r"mul\(\d{1,3},\d{1,3}\)", str(stringsWithoutDoAndDont))
        #print("allMultiplication: " + str(allMultiplication))
        for element in allMultiplication:
            #print("element: " + str(element))
            totalSum = totalSum + multiplication(str(element))
            
    print(totalSum)

def multiplication(moltiplicationFunction):
    allNumbers = re.findall(r"\d{1,3}", moltiplicationFunction)
    
    firstInt = int(allNumbers[0])
    secondInt = int(allNumbers[1])
    
    #print("firstInt: " + str(firstInt))
    #print("secondInd: " + str(secondInt))
    
    return firstInt*secondInt