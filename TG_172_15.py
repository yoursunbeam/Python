seconds=int(input('Введите количество секунд '))
if seconds>=60 and seconds<3600:
    minutes=seconds//60
    seconds=seconds%60
    print('время',minutes, 'минут',seconds,'секунд')
elif seconds>=3600 and seconds<86400:
    hours=seconds//3600
    minutes=seconds%3600//60
    seconds=seconds%3600%60
    print('время',hours,'часов',minutes, 'минут',seconds,'секунд')
elif seconds>=86400:
    days=seconds//86400
    hours=seconds%86400//3600
    minutes=seconds%86400%3600//60
    seconds=seconds%86400%3600%60
    print('время',days,'дней',hours,'часов',minutes, 'минут',seconds,'секунд')
else:
    print('время',seconds,'секунд')

    
    
