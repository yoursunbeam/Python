def main():
    
    x=int(input('Введите первое число '))
    y=int(input('Введите второе число '))
    numbers=[x]*y
    
    
    table=summa(numbers,0,y-1)
    print(table)
    
def summa(num,start,end):
    
    if start>end:
        return 0
    else:
        return num[start]+summa(num,start+1,end)
    
    
main()





        
        
