import random

print('Вам нужно будет отгадыть числа')
total=0
number=0
answer=0
again='д'

def play(number,answer,total):
    number=random.randint(1,100)
    answer=int(input('Введите число от 1 до 100 '))
    if number==answer:
       print('Поздравляем! Вы угадали!')
       number=random.randint(1,100)
       total=total+1
       print('Количество догадок',total)
    elif number<answer:
         print('Слишком много, попробуйте еще раз')
         total=total+1
         number=random.randint(1,100)
    else:
         print('Слишком мало, попробуйте еще раз')
         total=total+1
         number=random.randint(1,100)
         

while again=='д' or again=='Д':
      play(number,answer,total)
      again=input('Хотите сыграть еще?Нажмите д,если да ')
      
      
          





       

