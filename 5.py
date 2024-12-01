def pendulum(start, stop):
    swing = 0
    while start >= stop:
        swing += 1
        start -= start/100 * 8.4
    return f'Маятник считается остановившимся через {swing}'

start = float(input('Введите начальную амплитуду: '))
stop = float(input('Введите амплитуду остановки: '))
print(pendulum(start, stop))

