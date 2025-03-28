#import fileinput

def read_input_file(daySelected, isTest):
    filePath = "C:/Users/loren/.vscode/2024_AdventOfCode_Python/2024_AdventOfCode_Python/inputs/input"
    
    if(isTest):
        fileName = filePath + daySelected + "_test.txt"
    else:
        fileName = filePath + daySelected + ".txt"
    print(fileName)
    fileOpen = open(fileName, "r")
    
    return fileOpen