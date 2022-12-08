import random
number1=random.randint(100,999)
print(' ',number1)
number2=random.randint(100,999)
print('+',number2)
total=number1+number2
answer=int(input('Введите ваш ответ '))
if  total==answer:
    print('Поздравляем, ответ правильный!')
else:
    print(total)
