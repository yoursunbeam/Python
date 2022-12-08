import pickle
FILE='text572_4.dat'
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
               "\nДолжность:"+self.__positional+\
               "\nИдент.номер:"+self.__number
    
def main():
    
    again='д'
    
    output_file=open(FILE,'wb')

    while again.lower()=='д':
        
        name=input('Введите имя ')
        department=input('Введите отдел ')
        positional=input('Введите должность ')
        number=input('Введите идентификационный номер ')
        
        info=Employee(name,department,positional,number)
        
        pickle.dump(info,output_file)

        again=input('Хотите ввести следующие данные? (д\н):')
                    
    output_file.close()
    print('Данные записаны в ',FILE)

    end=False
    infile=open(FILE,'rb')
    while not end:
        try:
            contact1=pickle.load(infile)
            print(contact1)
        except EOFError:
            end=True
    infile.close()
    
    
       
main()




    



    
    
    

