import pickle
FILE='text572_6.dat'

class Patient:
    
    def __init__(self,name,address,number,sos):
        self.__name=name
        self.__address=address
        self.__number=number
        self.__sos=sos
        
        
    def set_name(self,name):
        self.__name=name

    def set_address(self,address):
        self.__address=address

    def set_number(self,number):
        self.__number=number

    def set_sos(self,sos):
        self.__sos=sos

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number

    def get_sos(self):
        return self.__sos

    def __str__(self):
        return "Пациент: "+self.__name+\
               "\nАдрес: "+self.__address+\
               "\nНомер телефона:"+self.__number+\
               "\nДля экстренной связи:"+self.__sos

    

class Procedure:
    
    def __init__(self,proc_name,date,doctor,cost):
        self.__proc_name=proc_name
        self.__date=date
        self.__doctor=doctor
        self.__cost=cost
        
        
    def set_proc_name(self,proc_name):
        self.__proc_name=proc_name

    def set_date(self,date):
        self.__date=date

    def set_doctor(self,doctor):
        self.__doctor=doctor

    def set_cost(self,cost):
        self.__cost=cost

    def get_proc_name(self):
        return self.__proc_name
    
    def get_date(self):
        return self.__date

    def get_doctor(self):
        return self.__doctor

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return "Наименование процедуры: "+self.__proc_name+\
               "\nДата: "+self.__date+\
               "\nВрач:"+self.__doctor+\
               "\nСтоимость:"+self.__cost

               
    
def main():
    
    again='д'
    
    output_file=open(FILE,'wb')

    name=input('Введите ФИО пациента ')
    address=input('Введите адрес и индекс ')
    number=input('Введите номер телефона ')
    sos=input('Введите данные для экстренной связи ')
    patient=Patient(name,address,number,sos)
    pickle.dump(patient,output_file)

    
    total=0
    while again.lower()=='д':
        
        proc_name=input('Введите наименование процедуры ')
        date=input('Введите дату процедуры ')
        doctor=input('Введите фамилию врача ')
        cost=input('Введите стоимость процедуры ')
        
       
        
        procedure=Procedure(proc_name,date,doctor,cost)
        cost=int(cost)
        total=total+cost
        
        pickle.dump(procedure,output_file)

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
    print('Итоговая стоимость процедур ',total)
    
       
main()




    



    
    
    

