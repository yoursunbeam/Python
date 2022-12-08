feet=float(input('Введите количество футов '))

def feet_to_inches(feet):
    inches=feet/12
    return inches

inches=feet_to_inches(feet)
print('Это равно',format(inches,'.2f'),'дюймов')
