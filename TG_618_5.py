def main():
    
    numbers=[10,10,10,10]
    
    table=summa(numbers,0,len(numbers)-1)
    print(table)
    
def summa(num,start,end):
    
    if start>end:
        return 0
    else:
        return num[start]+summa(num,start+1,end)
    
    
main()





        
        
