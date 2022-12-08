import pickle
FILE='text573_7.dat'

LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

class Employee:
    
    def __init__(self,name,department,positional,number):
        self.__name=name
        self.__department=department
        self.__positional=positional
        self.__number=number
        
    def set_name(self,name):
        self.__name=name

    def set_department(self,department):
        self.__department=department

    def set_positional(self,positional):
        self.__positional=positional

    def set_number(self,number):
        self.__number=number

    def get_name(self):
        return self.__name
    
    def get_department(self):
        return self.__department

    def get_positional(self):
        return self.__positional
    
    def get_number(self):
        return self.__number

    def __str__(self):
        return "Имя: "+self.__name+\
               "\nОтдел: "+self.__department+\
               "\nДолжность:"+self.__positional
               
    
def main():

    mycontacts=load_contacts()

    choice=0

    while choice!=QUIT:
        choice=get_menu_choice()

        if choice==LOOK_UP:
            look_up(mycontacts)
        elif choice==ADD:
            add(mycontacts)
        elif choice==CHANGE:
            change(mycontacts)
        elif choice==DELETE:
            delete(mycontacts)
        save_contacts(mycontacts)

def load_contacts():
    
    try:
        infile=open(FILE,'rb')
        contact=pickle.load(infile)
        infile.close()
    except IOError:
        contact={}
    return contact

def get_menu_choice():
    print()
    print('Меню')
    print('----------------------------')
    print('1.Найти сотрудника')
    print('2.Добавить нового сотрудника')
    print('3.Изменить данные о сотруднике')
    print('4.Удалить сотрудника')
    print('5.Выйти из программы')
    print()

    choice=int(input('Введите выбранный пункт: '))

    while choice<LOOK_UP or choice>QUIT:
        choice=int(input('Введите выбранный пункт: '))

    return choice

def look_up(mycontacts):
    number=int(input('Введите номер '))

    print(mycontacts.get(number,'Этот номер не найден'))

def add(mycontacts):
    name=input('Введите имя ')
    department=input('Введите отдел ')
    positional=input('Введите должность ')
    number=int(input('Введите идентификационный номер '))
        
    info=Employee(name,department,positional,number)

    if number not in mycontacts:
        mycontacts[number]=info
        print('Запись добавлена')
    else:
        print('Этот номер уже существует')

def change(mycontacts):
    
    number=int(input('Введите идентификационный номер '))
        
    if number in mycontacts:
        name=input('Введите измененное имя ')
        department=input('Введите новый отдел ')
        positional=input('Введите новую должность ')
        info=Employee(name,department,positional,number)
        mycontacts[number]=info
        print('информация обновлена')
    else:
        print('Этот номер не найден')

def delete(mycontacts):
    
    number=int(input('Введите идентификационный номер '))
        
    if number in mycontacts:
        del mycontacts[number]
        print('Запись удалена')
    else:
        print('Этот номер не найден')

def save_contacts(mycontacts):
    
    output_file=open(FILE,'wb')

    pickle.dump(mycontacts,output_file)

    output_file.close()    
       
       
main()




    



    
    
    

