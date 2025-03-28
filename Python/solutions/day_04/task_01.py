def solution(fileInput):
    xmas_matrix = [[]]
    row = 0
    column = 0
    matrix_already_initialize = False
    total_xmas = 0
    
    for line in fileInput:
        print(line)
        if not matrix_already_initialize:
            matrix_size = len(line) -1
            xmas_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
            matrix_already_initialize = True
            
        for char in line:
            #print('char: ' + char)
            if char == '\n':
               row += 1
               continue
            else:
               xmas_matrix [row] [column] = char
               column += 1
        
        column = 0   
    
    print(xmas_matrix)
    
    total_xmas += find_horizontal_xmas(xmas_matrix)
    total_xmas += find_vertical_xmas(xmas_matrix)
    total_xmas += find_diagonal_xmas(xmas_matrix)
    total_xmas += find_horizontal_reverse_xmas(xmas_matrix)
    total_xmas += find_vertical_reverse_xmas(xmas_matrix)
    total_xmas += find_diagonal_reverse_xmas(xmas_matrix)
                    
               
    
    
def find_horizontal_xmas(input_xmas_matrix):
    letter_to_find = ''
    previous_letter = ''
    xmas_found = 0
    for row in range(len(input_xmas_matrix)):
        letter_to_find = 'X'
        for column in range(len(input_xmas_matrix[row])) :
            if letter_to_find == 'X' and column >= len(input_xmas_matrix[row]) - 2 :
                continue
            elif letter_to_find == 'M' and column >= len(input_xmas_matrix[row]) - 1 :
                continue
            elif letter_to_find == 'A' and column == len(input_xmas_matrix[row]) :
                continue
            if input_xmas_matrix [row] [column] == letter_to_find :
                previous_letter = letter_to_find
                letter_to_find = next_letter_to_find(letter_to_find)
                if letter_to_find == 'X' and previous_letter == 'S' :
                    previous_letter = ''
                    print('row where XMAS found: ' + str(row))
                    xmas_found += 1
            elif input_xmas_matrix [row] [column] == 'X':
                letter_to_find = 'X'
                letter_to_find = next_letter_to_find(letter_to_find)
            else :
                letter_to_find = 'X'
                
        print(xmas_found)
    return xmas_found

def find_vertical_xmas(input_xmas_matrix):
    return 0

def find_diagonal_xmas(input_xmas_matrix):
    return 0

def find_horizontal_reverse_xmas(input_xmas_matrix):
    return 0

def find_vertical_reverse_xmas(input_xmas_matrix):
    return 0

def find_diagonal_reverse_xmas(input_xmas_matrix):
    return 0

def next_letter_to_find(letter_found):
    if letter_found == 'X' :
        return 'M'
    elif letter_found == 'M' :
        return 'A'
    elif letter_found == 'A' :
        return 'S'
    elif letter_found == 'S' :
        return 'X'