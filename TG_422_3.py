MONTHS=12

def sum(num):
    total=0
    for n in num:
        total=total+n
    print('Суммарное количество осадков',total)
    average=total/MONTHS
    print('Среднeе ежемесячное кол-во осадков',average)

def minmax(month):
   
    if month==0:
       print('January')
    elif month==1:
         print('February')
    elif month==2:
         print('March')
    elif month==3:
         print('April')
    elif month==4:
         print('May')
    elif month==5:
         print('June')
    elif month==6:
         print('July')
    elif month==7:
         print('August')
    elif month==8:
         print('September')
    elif month==9:
         print('October')
    elif month==10:
         print('November')
    else:
        print('December')
    
       
def main():
    rainfall=[]
    for i in range(1,MONTHS+1,1):
        value=float(input('Введите кол-во осадков за месяц '))
        rainfall.append(value)
    
    print(rainfall)
    
    sum(rainfall)
    
    
    monthmin=rainfall.index(min(rainfall))
    
    
    print('Самое низкое значение осадков было в ')
    minmax(monthmin)
    
   
    monthmax=rainfall.index(max(rainfall))
    
    
    print('Самое высокое значение осадков было в ')
    minmax(monthmax)
    
    

main()
    
