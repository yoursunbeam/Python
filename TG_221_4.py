speed=int(input('Введите скорость транспортного средства в км/ч '))
hours=int(input('Сколько часов оно двигалось '))
print('Час\tПройденное расстояние')
for hour in range(1,hours+1,1):
    distance=speed*hour
    print(hour,'\t',distance)
    
