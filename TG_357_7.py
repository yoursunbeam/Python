import random
def main():
    file=open('random.txt','w')
    count=int(input('Сколько чисел нужно записать в файл? '))
    for line in range(1,count+1,1):
        line=random.randint(1,500)
        file.write(str(line)+'\n')
    file.close()
    print('Данные успешно записаны в random.txt')

main()
