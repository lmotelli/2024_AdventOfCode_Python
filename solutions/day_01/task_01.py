#import read_input
import fileinput
import os.path

def distance_between_array():
    firstArray = []
    secondArray = [];
    
    fileName = input("please enter the file path:\n")
    fileOpen = open(fileName, "r")
    
    for line in fileOpen:
        splittedLine = line.split()
        firstArray.append(int(splittedLine[0]))
        secondArray.append(int(splittedLine[1]))

    if(len(firstArray) != len(secondArray)):
        return
    
    firstArray.sort();
    secondArray.sort();
    
    distanceArray = [];
    distance = 0;
    
    for index in range(len(firstArray)):
        distanceArray.append(abs(firstArray[index] -  secondArray[index]))
        distance += abs(firstArray[index] - secondArray[index])
    
    return distance

def read_input_file():
    fileName = input()
    fileOpen = open(fileName, "r")
    
    for line in fileOpen:
        print(line)

print(distance_between_array())