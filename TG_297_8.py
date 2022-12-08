wall_area=float(input('Площадь окрашиваемой поверхности '))
can_of_paint=float(input('Стоимость 5л банки краски ' ))
total=0

def number_of_cans(wall_area):
    cans=wall_area/10
    if (wall_area/10)<1:
        cans=1
        return cans
    elif (wall_area%10)>0:
         cans=int(cans+1)
         return cans
    else:
        return cans

def cost_of_paint(cans):
    cost=cans*can_of_paint
    return cost

def working_hours(wall_area):
    hours=wall_area*0.8
    return hours

def cost_of_work(hours):
    cost=hours*2000
    return cost

cans=number_of_cans(wall_area)
print('Банок с краской нужно',cans)
cost_c=cost_of_paint(cans)
print('Стоимость краски',cost_c)
hours=working_hours(wall_area)
print('Рабочих часов',hours)
cost_h=cost_of_work(hours)
print('Стоимость работы',cost_h)
total=cost_c+cost_h
print('Общая стоимость малярных работ',total)


