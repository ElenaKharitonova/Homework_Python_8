# Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите,
# сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def zadacha2():

    import random

    size_matrix = int(input('Введите размерность квадратной матрицы, кол-во строк = кол-во столбцов = : '))
    numbers = [0] * size_matrix
    temp = [0]

    for i in range(size_matrix):
        numbers[i] = [random.randint(1,100) for _ in range(size_matrix)]

    for row in numbers:
        print(row)
    
    diagonal_sum = 0

    for i in range(size_matrix):
        diagonal_sum = diagonal_sum + numbers[i][i]

    for index in range(len(numbers)):
        sum_in_row = sum(numbers[index])
        if sum_in_row > diagonal_sum:
            temp.append(index)

                
    if len(temp) - 1 < 1:
        print(f'Строк, в которых, сумма элементов строк > суммы главной диагонали (>{diagonal_sum}) нет')    
    else:
        print (f'Строка(-и), в которых, сумма элементов строки > суммы главной диагонали (>{diagonal_sum}):')
        for j in range(len(temp)-1):
            print (f' строка {temp[j+1]+1} {numbers[temp[j+1]]} - {sum(numbers[temp[j+1]])}')

zadacha2()  