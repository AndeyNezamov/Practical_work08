def count_numbers(num):
    first_num_count = 0
    temp = num
    while temp > 0:
        first_num_count += 1
        temp = temp // 10
    return  first_num_count

def change_number(num):
    last_digit = num % 10
    first_digit = num // 10 ** (count_numbers(num) - 1)
    between_digits = num % 10 ** (count_numbers(num) - 1) // 10
    num = last_digit * 10 ** (count_numbers(num) - 1) + between_digits * 10 + first_digit
    return num

def main():
    first_n = int(input("Введите первое число: "))
    second_n = int(input("Введите второе число: "))
    if count_numbers(first_n) < 3:
        return "В первом числе меньше трёх цифр."
    elif count_numbers(second_n) < 4:
        return 'Во втором числе меньше четырёх цифр.'
    else:
        return (f'Изменённое первое число: {change_number(first_n)}\n'
                f'Изменённое второе число: {change_number(second_n)}\n'
                f'Сумма чисел: {first_n + second_n}')

print(main())
