class Dog:
    def __init__(self,dogtype):
        self.__dogtype=dogtype
    def message(self):
        print('я-пес!')

class Poodle(Dog):
    def __init__(self):
        Dog.__init__(self,'пудель')
    def message(self):
        print('я-пудель!')

