def main():
    
    x=int(input('Введите основание '))
    y=int(input('Введите показатель степени '))
    numbers=[x]*y
    
    table=summa(numbers,0,y-1)
    print(table)
    
def summa(num,start,end):
    
    if start>end:
        return 1
    else:
        return num[start]*summa(num,start+1,end)
    
    
main()





        
        
