class Car:
    
    def __init__(self,year_model,make,speed):
        self.__year_model=year_model
        self.__make=make
        self.__speed=speed

    def set_year_model(self,year_model):
        self.__year_model=year_model

    def set_make(self,make):
        self.__make=make

    def set_speed(self,speed):
        self.__speed=speed

    def accelerate(self,five):
        self.__speed+=five

    def breake(self,five):
       self.__speed-=five
    
    def get_speed(self):
        return self.__speed

    def __str__(self):
        return "\nТекущая скорость:"+str(self.__speed)


def main():

    

    year_model=input('Введите модель ')
    make=input('Введите фирму-изготовитель ')
    speed=0
    car=Car(year_model,make,speed)
    for count in range(5):
        car.accelerate(5)
        print(car)

    for count in range(5):
        car.breake(5)
        print(car)
    

    
    print(car)

    

main()
    

