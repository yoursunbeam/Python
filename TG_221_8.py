print('это программа рассчитывает сумму положительных чисел')
print('введите отрицательное число, чтобы завершить работу')
number=int(input('Введите число '))
total=0
while number >0:
    total=total+number
    number=int(input('Введите число '))
print('Сумма чисел=',total)

