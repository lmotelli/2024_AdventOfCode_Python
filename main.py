from utils.read_input import read_input_file
from utils.invoke_correct_solution import find_solution

import sys

def main():
    sys.stdout.flush()
    day = input("enter the day:\n")
    if(int(day) < 10):
            day = "0" + day
            print("new day: " + day )
    isTest = input("do you want to test?\n").strip().lower() in ["yes", "y", "true", "1"]
    
    fileOpen = read_input_file(day, isTest)
    
    solution_one_or_two = input("select solution one or two:\n")
    
    #print(find_solution(day, solution_one_or_two, fileOpen))
    find_solution(day, solution_one_or_two, fileOpen)
    
main()