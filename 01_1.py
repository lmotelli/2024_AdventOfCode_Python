import fileinput

def distance_between_array():
    firstArray = [int(x) for x in input().split()];
    secondArray = [int(x) for x in input().split()];

    if(len(firstArray) != len(secondArray)):
        return
    
    firstArray.sort();
    secondArray.sort();
    
    distanceArray = [];
    distance = 0;
    
    for index in range(len(firstArray)):
        distanceArray.append(abs(firstArray[index] -  secondArray[index]))
        distance += abs(firstArray[index] -  secondArray[index])
    
    return distance

#def read_input_file():
    #fileName = input()
    #fileOpen = open(fileName, "r")
    #for line in fileinput.input(encoding="UTF-8"):
    #for line in fileOpen:
        #print(line)
    
#read_input_file()
print(distance_between_array())