length_ridge=float(input('Введите длину гряды в м '))
supports=float(input('Сколько метров занимают концевые опоры? '))
vines=float(input('Сколько метров между лозами? '))
number_vines=int((length_ridge-2*supports)/vines)
print('Количество виноградных лоз=',number_vines)


