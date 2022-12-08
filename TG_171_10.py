kopecks5=int(input('Введите количество 5-копеечных монет '))
kopecks10=int(input('Введите количество 10-копеечных монет '))
kopecks50=int(input('Введите количество 50-копеечных монет '))
if (kopecks5*5+kopecks10*10+kopecks50*50)==100:
    print('Поздравляем, Вы выиграли!')
elif (kopecks5*5+kopecks10*10+kopecks50*50)>100:
    print('Вы ввели сумму больше рубля')
else:
    print('Вы ввели сумму меньше рубля')
    
   
