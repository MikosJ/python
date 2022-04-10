import random

def matrix_numbers(columns, rows, min_range, max_range):
    numbers = [[random.randint(min_range, max_range) for i in range(0,columns)] for j in range(0,rows)]
    return numbers

def matrix_file(path, matrix):
    matrix_string = ""

    for i in range(0,len(matrix)):
        if i != 0:
            matrix_string += "\n"
        for j in range(0,len(matrix[i])):
            matrix_string += str(matrix[i][j]) + "\t"
        
    with open(path, "x") as save_file:
        save_file.write(matrix_string)

def matrix_column_sum_mean(matrix, column):
    sum = 0
    for i in range(0,len(matrix)):
        sum += matrix[i][column]
    mean = sum/len(matrix)
    return sum, mean, column

def matrix_sum_mean_file(sum, mean, column, path):
    with open(path, "x") as file_write:
        file_write.write(f"Sum of numbers in a column #{column} = {sum}, mean of numbers in a column number {column} = {mean}")
    file_write.close()
    

def matrix_sum_list(matrix):
    column_sum = []
    for i in range(0,len(matrix[0])):
        sum = 0
        for j in range(0,len(matrix)):
            sum += matrix[j][i]
        column_sum.append(sum)
    return column_sum

def matrix_sum_list_file(sum_list, path):
    with open(path, "x") as file_write:
        for i in sum_list:
            file_write.write(f"Sum of integers in column #{sum_list.index(i)} is {i}\n")

def diagonal_sum(matrix):
    sum = 0
    if len(matrix) == len(matrix[0]):
        for i in range(0,len(matrix)):
            sum += matrix[i][i]
    else:
        return
    return sum
        
        
    
matrix_a = matrix_numbers(5,3,1,10)
sum_mean = matrix_column_sum_mean(matrix_a,0)
column_sum_list = matrix_sum_list(matrix_a)

matrix_file("C:\\Users\\kubam\\desktop\\macierz.txt", matrix_a)
matrix_sum_mean_file(*sum_mean, "C:\\Users\\kubam\\desktop\\sumasrednia.txt")
matrix_sum_list_file(column_sum_list, "C:\\Users\\kubam\\desktop\\lista.txt")
print(matrix_a)
print(matrix_sum_list(matrix_a))
print(diagonal_sum(matrix_a))
