class Beverage:
    def __init__(self,bev_name):
        self.__bev_name=bev_name
    def message(self):
        print('я-напиток!')

class Cola(Beverage):
    def __init__(self):
        Beverage.__init__(self,'кока-кола')
    def message(self):
        print('я-Кола!')


def main():
    p=Beverage('саженец')
    t=Cola()
    p.message()
    t.message()

main()
