numbers=[1,2,3,4,5,6,7,8,9,10]
n=int(input('Введите число '))
def main(listik,num):
    listik.sort()
    if num in numbers:
        item=listik.index(num)
        print(listik[item+1:])
    else:
        print('Такого элемента в списке нет')

main(numbers,n)
    
