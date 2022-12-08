import pickle
FILE='text572_5.dat'
class RetailItem:
    
    def __init__(self,product,quantity,price):
        self.__product=product
        self.__quantity=quantity
        self.__price=price
        
    def set_product(self,product):
        self.__product=product

    def set_quantity(self,quantity):
        self.__quantity=quantity

    def set_price(self,price):
        self.__price=price

    def get_product(self):
        return self.__product
    
    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price
    

    def __str__(self):
        return "Товар: "+self.__product+\
               "\nКоличество на складе: "+self.__quantity+\
               "\nЦена:"+self.__price
               
    
def main():
    
    again='д'
    
    output_file=open(FILE,'wb')

    while again.lower()=='д':
        
        product=input('Введите наименование товара ')
        quantity=input('Введите количество ')
        price=input('Введите цену ')
       
        
        info=RetailItem(product,quantity,price)
        
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




    



    
    
    

