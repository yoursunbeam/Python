print('Вам нужно будет ввести расходы на автомобиль в месяц')
loan_payment=int(input('Платеж по кредиту '))
insurance=int(input('Страховка '))
petrol=int(input('Бензин '))
engine_oil=int(input('Машинное масло '))
tires=int(input('Шины '))
maintenance=int(input('Техобслуживание '))

def get_monthly_cost(a,b,c,d,e,f):
    monthly_cost=a+b+c+d+e+f
    print('Сумма расходов за месяц ',monthly_cost)

def get_annual_cost(a,b,c,d,e,f):
    annual_cost=(a+b+c+d+e+f)*12
    print('Сумма расходов за год ',annual_cost)

get_monthly_cost(loan_payment,insurance,petrol,engine_oil,tires,maintenance)

get_annual_cost(loan_payment,insurance,petrol,engine_oil,tires,maintenance)
