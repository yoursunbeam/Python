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

    

class ShiftSupervisor(Employee):
    def __init__(self,name,number,salary,prize):
        Employee.__init__(self,name,number)
        self.__salary=salary
        self.__prize=prize
        
    def set_salary(self,salary):
        self.__salary=salary

    def set_prize(self,prize):
        self.__prize=prize

    def get_salary(self):
        return self.__salary

    def get_prize(self):
        return self.__prize


def main():
    name=input('Введите имя сотрудника:')
    number=int(input('Введите идентификационный номер: '))
    salary=int(input('Введите годовой оклад: '))
    prize=float(input('Введите производственную премию: '))
    info=ShiftSupervisor(name,number,salary,prize)
    print('Сотрудник: ',name)
    print('Номер: ',number)
    print('Оклад: ',salary)
    print('Премия:',prize)
    
main()
