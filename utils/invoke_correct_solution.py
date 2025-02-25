from solutions.day_01 import task_01 as day01_01
from solutions.day_01 import task_02 as day01_02
from solutions.day_02 import task_01 as day02_01
from solutions.day_02 import task_02 as day02_02
from solutions.day_03 import task_01 as day03_01
from solutions.day_03 import task_02 as day03_02
from solutions.day_04 import task_01 as day04_01
from solutions.day_04 import task_02 as day04_02
from solutions.day_05 import task_01 as day05_01
from solutions.day_05 import task_02 as day05_02
from solutions.day_06 import task_01 as day06_01
from solutions.day_06 import task_02 as day06_02
from solutions.day_07 import task_01 as day07_01
from solutions.day_07 import task_02 as day07_02
from solutions.day_08 import task_01 as day08_01
from solutions.day_08 import task_02 as day08_02
from solutions.day_09 import task_01 as day09_01
from solutions.day_09 import task_02 as day09_02
from solutions.day_10 import task_01 as day10_01
from solutions.day_10 import task_02 as day10_02
from solutions.day_11 import task_01 as day11_01
from solutions.day_11 import task_02 as day11_02
from solutions.day_12 import task_01 as day12_01
from solutions.day_12 import task_02 as day12_02
from solutions.day_13 import task_01 as day13_01
from solutions.day_13 import task_02 as day13_02
from solutions.day_14 import task_01 as day14_01
from solutions.day_14 import task_02 as day14_02
from solutions.day_15 import task_01 as day15_01
from solutions.day_15 import task_02 as day15_02
from solutions.day_16 import task_01 as day16_01
from solutions.day_16 import task_02 as day16_02
from solutions.day_17 import task_01 as day17_01
from solutions.day_17 import task_02 as day17_02
from solutions.day_18 import task_01 as day18_01
from solutions.day_18 import task_02 as day18_02
from solutions.day_19 import task_01 as day19_01
from solutions.day_19 import task_02 as day19_02
from solutions.day_20 import task_01 as day20_01
from solutions.day_20 import task_02 as day20_02
from solutions.day_21 import task_01 as day21_01
from solutions.day_21 import task_02 as day21_02
from solutions.day_22 import task_01 as day22_01
from solutions.day_22 import task_02 as day22_02
from solutions.day_23 import task_01 as day23_01
from solutions.day_23 import task_02 as day23_02
from solutions.day_24 import task_01 as day24_01
from solutions.day_24 import task_02 as day24_02
from solutions.day_25 import task_01 as day25_01
from solutions.day_25 import task_02 as day25_02

def find_solution(day, task_number, inputFile):
    # Define a dictionary with all possible (day, task) pairs
    solutions = {
        "01": {"1": day01_01.solution, "2": day01_02.solution},
        "02": {"1": day02_01.solution, "2": day02_02.solution},
        "03": {"1": day03_01.solution, "2": day03_02.solution},
        "04": {"1": day04_01.solution, "2": day04_02.solution},
        "05": {"1": day05_01.solution, "2": day05_02.solution},
        "06": {"1": day06_01.solution, "2": day06_02.solution},
        "07": {"1": day07_01.solution, "2": day07_02.solution},
        "08": {"1": day08_01.solution, "2": day08_02.solution},
        "09": {"1": day09_01.solution, "2": day09_02.solution},
        "10": {"1": day10_01.solution, "2": day10_02.solution},
        "11": {"1": day11_01.solution, "2": day11_02.solution},
        "12": {"1": day12_01.solution, "2": day12_02.solution},
        "13": {"1": day13_01.solution, "2": day13_02.solution},
        "14": {"1": day14_01.solution, "2": day14_02.solution},
        "15": {"1": day15_01.solution, "2": day15_02.solution},
        "16": {"1": day16_01.solution, "2": day16_02.solution},
        "17": {"1": day17_01.solution, "2": day17_02.solution},
        "18": {"1": day18_01.solution, "2": day18_02.solution},
        "19": {"1": day19_01.solution, "2": day19_02.solution},
        "20": {"1": day20_01.solution, "2": day20_02.solution},
        "21": {"1": day21_01.solution, "2": day21_02.solution},
        "22": {"1": day22_01.solution, "2": day22_02.solution},
        "23": {"1": day23_01.solution, "2": day23_02.solution},
        "24": {"1": day24_01.solution, "2": day24_02.solution},
        "25": {"1": day25_01.solution, "2": day25_02.solution},
    }

    # Retrieve and execute the correct function if it exists, otherwise print an error
    if day in solutions and task_number in solutions[day]:
        solutions[day][task_number](inputFile)
    else:
        print("error")
