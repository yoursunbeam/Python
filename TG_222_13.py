start=int(input('Cтартовое количество организмов '))
increase=int(input('Среднесуточное увеличение в % '))
days=int(input('Количество дней для размножения '))
print('День\tПопуляция')
total=0
population=start
print(1,'\t',population)
for day in range (2,days+1,1):
    population=population*(100+increase)/100    
    print(day,'\t',population)
