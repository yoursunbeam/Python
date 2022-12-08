age=float(input('Введите возраст '))
if age<=1:
    print('младенец')
elif age>1 and age<13:
    print('ребенок')
elif age>=13 and age<20:
    print('подросток')
else:
    print('взрослый')
    
