cost=float(input('Введите стоимость еды '))
tip=cost*0.18
tax=cost*0.07
total_amount=cost+tip+tax
print('Стоимость еды=',format(cost,'.2f'))
print('Чаевые=',format(tip,'.2f'))
print('Налог с продаж=',format(tax,'.2f'))
print('Итого=',format(total_amount,'.2f'))
