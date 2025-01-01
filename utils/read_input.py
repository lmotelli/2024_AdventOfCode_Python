import fileinput

def read_input_file():
    filePath = "C:\Users\loren\.vscode\2024_AdventOfCode_Python\2024_AdventOfCode_Python\inputs\input"
    day = input("enter the day")
    isTest = input("do you want to test/debug?")
    
    if(isTest):
        fileName = filePath + day + "_test.txt"
    else:
        fileName = filePath + day + ".txt"
    fileOpen = open(fileName, "r")
    
    return fileOpen