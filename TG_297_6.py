fats=int(input('Количество жиров в граммах '))
carbohydrarates=int(input('количество углеводов в граммах '))

def calories_from_fats(fats):
    calories=fats*9
    print('Калории полученные из жиров=',calories)

def calories_from_carbohydrarates(carbohydrarates):
    calories=carbohydrarates*4
    print('Калории полученные из жиров=',calories)

calories_from_fats(fats)
calories_from_carbohydrarates(carbohydrarates)
