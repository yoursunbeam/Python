import random
N=int(input('Введите число больше или равно 3: '))

def main():
    array_2=[]
    
    for c in range(N):
        array_1=[]
        for r in range(N):
            num=random.randint(1,100)
            array_1.append(num)
        array_2.append(array_1)
            
    print('Двумерный массив:')
    print(array_2)
    
    name_list=[]
    i=0
    for r in range(N):
        number=array_2[r][N-1-i]
        name_list.append(number)
        i=i+1

    print('Элементы побочной диагонали:')
    print(name_list)
    print('Минимальный элемент побочной диагонали=',min(name_list))
    

main()
