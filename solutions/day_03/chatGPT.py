import re

def process_memory_string(memory_string):
    # Regular expressions to identify relevant instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    enabled = True  # At the beginning, mul instructions are enabled
    total_sum = 0

    # Split memory string by non-alphanumeric characters while keeping important tokens
    tokens = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory_string)

    for token in tokens:
        if do_pattern.fullmatch(token):
            enabled = True
        elif dont_pattern.fullmatch(token):
            enabled = False
        else:
            match = mul_pattern.fullmatch(token)
            if match and enabled:
                a, b = map(int, match.groups())
                total_sum += a * b

    return total_sum

# Read input file
with open("C:/Users/loren/.vscode/2024_AdventOfCode_Python/2024_AdventOfCode_Python/inputs/input03.txt", "r") as file:
    memory_string = file.read().strip()

# Process and print the result
result = process_memory_string(memory_string)
print("Sum of enabled multiplications:", result)
