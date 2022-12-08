budget=float(input('Введите сумму денег на месяц '))
cost=int(input('Введите количество статей расходов '))
total=0
for counter in range(cost):
    expenses=float(input('Введите суммы по статьям расходов '))
    total=total+expenses
    
profit=budget-total
if profit==0:
    print('Вы ничего не сэкономили')
if profit<0:
    print('Вы потратили больше,чем у вас было',profit)
if profit>0:
   print('Ваша прибыль составила ',profit)

