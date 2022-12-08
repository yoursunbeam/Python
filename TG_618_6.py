def main():

    n=int(input('Введите число '))
    numbers=[]
    for i in range(1,n+1,1):
        numbers.append(i)
    print(numbers)
    
    table=summa(numbers,0,len(numbers)-1)
    print(table)
    
def summa(num,start,end):
    
    if start>end:
        return 0
    else:
        return num[start]+summa(num,start+1,end)
    
    
main()





        
        

        
        
