#import read_input
#import fileinput
#import os.path

def solution(inputFile):
    firstArray = []
    secondArray = []
    
    #fileName = input("please enter the file path:\n")
    #fileOpen = open(fileName, "r")
    
    for line in inputFile:
        splittedLine = line.split()
        firstArray.append(int(splittedLine[0]))
        secondArray.append(int(splittedLine[1]))

    if(len(firstArray) != len(secondArray)):
        return
    
    firstArray.sort()
    secondArray.sort()
    
    distanceArray = []
    distance = 0
    
    for index in range(len(firstArray)):
        distanceArray.append(abs(firstArray[index] -  secondArray[index]))
        distance += abs(firstArray[index] - secondArray[index])
    print(distance)
    #return distance