
def sum(num):
    total=0
    for n in num:
        total=total+n
    print('Сумма чисел=',total)
    average=total/20
    print('Среднeе арифметическое=',average)


       
def main():
    numbers=[]
    print('Введите 20 чисел через Enter')
    for i in range(1,21,1):
        value=int(input())
        numbers.append(value)
    
    print(numbers)
    
    sum(numbers)
    print('Минимальное число=',min(numbers))
    
    print('Максимальное число=',max(numbers))
    
    

main()
    
