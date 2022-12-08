class Information:
    
    def __init__(self,name,address,age,number):
        self.__name=name
        self.__address=address
        self.__age=age
        self.__number=number
        
    def set_name(self,name):
        self.__name=name

    def set_address(self,address):
        self.__address=address

    def set_age(self,age):
        self.__age=age

    def set_number(self,number):
        self.__number=number

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age
    
    def get_number(self):
        return self.__number

    def __str__(self):
        return "Имя: "+self.__name+\
               "\nАдрес: "+self.__address+\
               "\nВозраст:"+self.__age+\
               "\nТел.номер:"+self.__number
    
def main():

    def contact():
        name=input('Введите имя ')
        address=input('Введите адрес ')
        age=input('Введите возраст ')
        number=input('Введите тел.номер ')
        info=Information(name,address,age,number)
        print(info)
    contact()
    
    contact()
    
    contact()
    
        
main()




    



    
    
    

