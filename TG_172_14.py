height=float(input('Введите рост в метрах '))
weight=float(input('Введите вес в кг '))
BMI=weight/(height**2)
if BMI<18.5:
    print('Недостаток веса')
elif BMI>=18.5 and BMI<=25:
    print('Оптимальный вес')
else:
    print('Избыточный вес')
    
