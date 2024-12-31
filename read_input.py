import fileinput

def read_input_file():
    fileName = input("please enter the file path:\n")
    fileOpen = open(fileName, "r")
    
    array1 = []
    array2 = []
    
    for line in fileOpen:
        splittedLine = line.split()
        array1.append(splittedLine[0])
        array2.append(splittedLine[1])
        
    print("array1:\n")
    for singleElement in array1:
        print(singleElement)
    print("array2:\n")
    for singleElement in array2:
        print(singleElement)
    
    fileOpen.close()
    
read_input_file()