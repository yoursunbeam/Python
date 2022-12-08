years=int(input('Введите количество лет '))
total=0

for year in range(years):
    for month in range(1,13,1):
        rainfall=int(input('Введите количество осадков в мм '))
        total=rainfall+total
        
months=years*12
average=total/months
print('Общее количество месяцев ',months)
print('Общее количество мм осадков',total)
print('Среднее количество осадков за весь период',average)
