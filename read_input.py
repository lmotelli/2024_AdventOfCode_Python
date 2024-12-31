import fileinput

def read_input_file():
    fileName = input()
    fileOpen = open(fileName, "r")
    
    for line in fileOpen:
        print(line)