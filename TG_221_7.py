days=int(input('Введите количество дней '))
print('День\tЗарплата')

total=0

for day in range(days+1):
    penny=1*2**(day-1)
    total=total+penny
    if (penny and day)>=1:
        print(day,'\t',penny)
ruble=total/100
print('Зарплата за весь период',ruble,'рублей')

