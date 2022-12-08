def main():
    number=input('введите ряд однозначных чисел без пробелов ')
    index=0
    total=0
    new=[]
    while index<len(number):
        num=number[index]
        new.append(num)
        index=index+1
    print(new)
        
    index=0

    while index<len(new):
        new[index]=int(new[index])
        index=index+1

    for i in new:
        total=total+i
    print('сумма цифр=',total)
        
     
        

main()
