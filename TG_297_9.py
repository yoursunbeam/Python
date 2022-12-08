def main():
    
     monthly_sales=float(input('Объем продаж за месяц '))
     
    
     federal_tax=get_federal_tax(monthly_sales)
     print('Федеральный налог с продаж=',format(federal_tax,'.2f'))
     
     municipal_tax=get_municipal_tax(monthly_sales)
     print('Региональный налог с продаж=',format(municipal_tax,'.2f'))

     general_tax=get_general_tax(federal_tax,municipal_tax)
     print('Общий налог с продаж=',format(general_tax,'.2f'))

     
def get_federal_tax(monthly_sales):
    federal_tax=monthly_sales*0.05
    return federal_tax

def get_municipal_tax(monthly_sales):    
    municipal_tax=monthly_sales*0.025
    return municipal_tax

def get_general_tax(a,b):
    general_tax=a+b
    return  general_tax  


main()
