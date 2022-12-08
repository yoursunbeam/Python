import random
def main():
    file=open('random.txt','r')
    line=file.readline()
    total=0
    count=0
    while line!='':
        amount=int(line)
        print(amount)
        total=amount+total
        count=count+1
        line=file.readline()
    
    print('Сумма чисел',total)
    print('Количество чисел в файле',count)
    file.close()
   

main()
