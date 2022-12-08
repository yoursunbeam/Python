class Employee:
    def __init__(self,name,number):
        self.__name=name
        self.__number=number
        
    def set_name(self,name):
        self.__name=name

    def set_number(self,number):
        self.__number=number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    

class ProductionWorker(Employee):
    def __init__(self,name,number,shift,rate):
        Employee.__init__(self,name,number)
        self.__shift=shift
        self.__rate=rate
        
    def set_name(self,shift):
        self.__shift=shift

    def set_rate(self,rate):
        self.__rate=rate

    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate


def main():
    name=input('Введите имя сотрудника:')
    number=int(input('Введите идентификационный номер: '))
    shift=int(input('Введите смену,дневная - 1,вечерняя - 2: '))
    rate=float(input('Введите почасовую ставку оплаты труда: '))
    info=ProductionWorker(name,number,shift,rate)
    print('Сотрудник: ',name)
    print('Номер: ',number)
    print('Смена: ',shift)
    print('Ставка:',rate)
    
main()
