money=int(input('Введите сумму денег на счете '))
months=int(input('Введите длительность вклада в месяцах '))
month_rate=float(input('Введите ежемесячную ставку в % '))
year_rate=month_rate*12
days_in_period=months*30

def income(P,I,t):
    a=t/365
    b=I*a
    c=1+b
    d=c/100
    f=P*d
    return f

new_money=income(money,year_rate,days_in_period)
print('На счете через',months,'месяцев будет',new_money)
