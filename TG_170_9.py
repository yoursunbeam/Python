pocket=int(input('Введите номер кармана '))
if pocket==0:
    print('зеленый')
elif pocket>=1 and pocket<=10:
    if pocket%2==0:
        print('черный')
    else:
        print('красный')
elif pocket>=11 and pocket<=18:
    if pocket%2==0:
        print('красный')
    else:
        print('черный')
elif pocket>=19 and pocket<=28:
    if pocket%2==0:
        print('черный')
    else:
        print('красный')
elif pocket>=29 and pocket<=36:
    if pocket%2==0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка, введите число от 0 до 36')
    
    
