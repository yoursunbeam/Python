weight=int(input('Введите массу тела в кг '))
speed=int(input('Введите скорость тела в м/с '))
def kinetic_energy(m,v):
    k=0.5*m*v
    print('Кинетическая энергия =',k)

kinetic_energy(weight,speed)
