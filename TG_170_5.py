m=int(input('Введите массу тела '))
F=m*9.8
if F>500:
    print('Тело слишком тяжелое')
elif F<100:
    print('Тело слишком легкое')
else:
    print('вес тела=',F)