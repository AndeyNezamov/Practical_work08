def reverse_number(num):
    revers = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        revers = revers * 10
        revers = revers + digit
    return revers

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

print(f'Первое число наоборот: {reverse_number(number_1)}\nВторое число наоборот: {reverse_number(number_2)}')

