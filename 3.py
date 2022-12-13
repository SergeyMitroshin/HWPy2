# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
x = int(input('Введите число: '))
div = 1
while div <= x:
    div = div + 1
    if x % div == 0:
        print(div)
        break