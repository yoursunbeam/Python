class Plant:
    def __init__(self,plant_type):
        self.__plant_type=plant_type
    def message(self):
        print('я-растение!')

class Tree(Plant):
    def __init__(self):
        Plant.__init__(self,'дерево')
    def message(self):
        print('я-дерево!')


def main():
    p=Plant('саженец')
    t=Tree()
    p.message()
    t.message()

main()
