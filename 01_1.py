import read_input

def distance_between_array():
    firstArray = [int(x) for x in read_input.read_input_file()];
    secondArray = [int(x) for x in read_input.read_input_file()];

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

print(distance_between_array())