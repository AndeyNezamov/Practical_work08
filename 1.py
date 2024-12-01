start_number = float(input("Введите число: "))
if start_number > 1:
    count = 0
    while start_number > 10:
        count += 1
        start_number /= 10

    print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")
else:
    count = 0
    while start_number < 1:
        count += 1
        start_number *= 10
    print(f"Формат плавающей точки: x = {start_number} * 10 ** -{count}")