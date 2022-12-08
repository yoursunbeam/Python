DAYS=7

def sum(num):
    total=0
    for n in num:
        total=total+n
    print('Сумма значений в списке=',total)
    
def main():
    sales=[]
    for i in range(1,DAYS+1,1):
        value=float(input('Введите продажи за день '))
        sales.append(value)
    print(sales)
    
    sum(sales)
    

main()
    
