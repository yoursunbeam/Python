class Person:
    def __init__(self,name,address,number):
        self.__name=name
        self.__address=address
        self.__number=number
        
    def set_name(self,name):
        self.__name=name

    def set_number(self,address):
        self.__address=address

    def set_number(self,number):
        self.__number=number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number

    

class Customer(Person):
    def __init__(self,name,address,number,client,mail):
        Person.__init__(self,name,address,number)
        self.__name=name
        self.__address=address
        self.__number=number
        
    def set_client(self,client):
        self.__client=client

    def set_mail(self,mail):
        self.__mail=mail

    def get_client(self):
        return self.__client

    def get_mail(self):
        return self.__mail


def main():

    def mailing(c):
        a=False
        if mail==1:
            a=True
            print('Согласен на рассылку')
        elif mail==0:
            a=False
            print('Не согласен на рассылку')
        else:
            print('1-да,0-нет')
            
    name=input('Введите имя сотрудника:')
    address=input('Введите адрес сотрудника:')
    number=int(input('Введите телефонный номер: '))
    client=int(input('Введите номер клиента: '))
    mail=int(input('Согласие на расслыку, да-1, нет- 0 '))
    
    info=Customer(name,address,number,client,mail)
    print('Сотрудник: ',name)
    print('Адрес: ',address)
    print('Тел.номер: ',number)
    print('Номер клиента: ',client)
    mailing(mail)
    
main()
