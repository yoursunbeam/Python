actual_cost=int(input('Фактическая стоимость недвижимости '))



def get_estimated_cost(actual_cost):
    estimated_cost=actual_cost*0.6
    return estimated_cost
    

def get_property_cost(estimated_cost):
    property_cost=estimated_cost*0.0072
    return property_cost

    
estimated_cost=get_estimated_cost(actual_cost)
print('Оценочная стоимость недвижимости ',estimated_cost)

property_cost=get_property_cost(estimated_cost)
print('Налог на имущество ',property_cost)





