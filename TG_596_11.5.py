class Vegetable:
    def __init__(self,vegtype):
        self.__vegtype=vegtype
    def message(self):
        print('я-овощ!')

class Potato(Vegetable):
    def __init__(self):
        Vegetable.__init__(self,'картофель')
    def message(self):
        print('я-картофель!')

def main():
    v=Vegetable('овощной продукт')
    p=Potato()
    v.message()
    p.message()

main()
