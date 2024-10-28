A = float(input(f'Введите значение давления, А: '))

epsilon = float(input(f'Введите значение отклонения: '))

N = int(input(f'Введите время тестирования: '))

unacceptable_count = 0

for i in range(N):

    reading = float(input(f'Показания датчика: '))

    deviation = abs(reading - A)

    if deviation > epsilon:
        unacceptable_count += 1

print(f'Количество отклонений: {unacceptable_count}')
