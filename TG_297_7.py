a_class=int(input('Сколько билетов класса А продано? '))
b_class=int(input('Сколько билетов класса В продано? '))
c_class=int(input('Сколько билетов класса С продано? '))

def income(a,b,c):
    sum_of_income=a*20+b*15+c*10
    print('Доход от продажи билетов ',sum_of_income,'$')

income(a_class,b_class,c_class)

