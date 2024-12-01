def maximum_of_two(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def maximum_of_three(num_1, num_2, num_3):
    if maximum_of_two(num_1, num_2) > num_3:
        return f'Самое большое число: {maximum_of_two(num_1, num_2)}'
    else:
        return f'Самое большое число: {num_3}'

number_1 = int(input('Введите число: '))
number_2 = int(input('Введите число: '))
number_3 = int(input('Введите число: '))

print(maximum_of_three(number_1, number_2, number_3))