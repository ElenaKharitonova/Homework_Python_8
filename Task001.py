# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
# заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
# наилучшим средним баллом.
def zadacha1():
    
    import random

    group_count = int(input('Введите количество групп: '))
     
    marks = [0] * group_count

    for i in range(group_count):
        marks[i] = [random.randint(1,5) for _ in range(random.randint(20,30))]
    for row in marks:
        print(row)
    
    mark_max = 0
    group_max = 0

    for i in range(group_count):
        average_mark = 0
        students_count = len(marks[i])
        for j in range(students_count):
            average_mark = average_mark + marks[i][j]
        average_mark = average_mark / students_count
        # print(round(average_mark, 2))
        if average_mark > mark_max:
            mark_max = average_mark
            group_max = i
    print(f'Максимальный средний бал у группы {group_max + 1}, равен {round(mark_max, 2)}')
    
zadacha1()