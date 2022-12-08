import pickle




LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

def main():
    end_of_file=False
    input_file=open('mydata509_8.dat','rb')
    while not end_of_file:
        try:
            file=pickle.load(input_file)
            display(mail)
        except EOFError:
            end_of_file=True
    input_file.close()
    outputfile=open('mydata509_8.dat','wb')
    mail={}

    choice=0

    while choice!=QUIT:
        choice=get_menu_choice()

        if choice==LOOK_UP:
            look_up(mail)
        elif choice==ADD:
            add(mail)
        elif choice==CHANGE:
            change(mail)
        elif choice==DELETE:
            delete(mail)
def get_menu_choice():
    print()
    print('Имена и адреса электронной почты: ')
    print('----------------------------------')
    print('1.Найти адрес электронной почты ')
    print('2.Добавить новое имя и адрес электронной почты')
    print('3.Изменить адрес электронной почты')
    print('4.Удалить адрес электронной почты')
    print('5.Выйти из программы')
    print()

    choice=int(input('Введите выбранный пункт меню '))

    while choice<LOOK_UP or choice>QUIT:
        choice=int(input('Введите выбранный пункт меню '))

    return choice

    pickle.dump(mail,outputfile)
    outputfile.close()

def look_up(mail):
    name=input('Введите имя ')

    print(mail.get(name,'Не найдено'))

def add(mail):
    name=input('Введите имя ')
    email=input('Введите адрес электронной почты ')

    if name not in mail:
        mail[name]=email
    else:
        print('Такая запись уже существует')

def change(mail):
    name=input('Введите имя ')

    if name in mail:
        email=input('Введите новый адрес электронной почты ')
        mail[name]=email
        
    else:
        print('Это имя не найдено')

def delete(mail):
    name=input('Введите имя ')

    if name in mail:
        del mail[name]
        
    else:
        print('Это имя не найдено')

def display(mail):
    print('Имя ', mail[name])
    print('Email',mail[email])

main()

    
