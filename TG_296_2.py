def main():
    
     purchase_price=float(input('Введите величину покупки '))
     print('Сумма покупки=',purchase_price)
    
     federal_tax=get_federal_tax(purchase_price)
     print('Федеральный налог с продаж=',format(federal_tax,'.2f'))
     regional_tax=get_regional_tax(purchase_price)
     print('Региональный налог с продаж=',format(regional_tax,'.2f'))

     general_tax=get_general_tax(federal_tax,regional_tax)
     print('Общий налог с продаж=',format(general_tax,'.2f'))

     total_amount=get_total_amount(purchase_price,general_tax)
     print('Общая сумма продажи=',format(total_amount,'.2f'))


def get_federal_tax(purchase_price):
    federal_tax=purchase_price*0.05
    return federal_tax

def get_regional_tax(purchase_price):    
    regional_tax=purchase_price*0.025
    return regional_tax

def get_general_tax(a,b):
    general_tax=a+b
    return  general_tax  

def get_total_amount(a,b):
    total_amount=a+b
    return total_amount
    


main()
   


