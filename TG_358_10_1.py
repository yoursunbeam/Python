def main():
    num=int(input('Сколько записей вы хотите создать?'))
    file=open('golf.txt','w')
    for count in range(1,num+1,1):
        print('Введите имя игрока и его счет в игре')
        name=input('Имя: ')
        score=input('Счет: ')

        file.write(name+'\n')
        file.write(score+'\n')

    file.close()
    print('Записи сохранены')
main()


