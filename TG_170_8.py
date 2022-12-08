person=int(input('Введите количество участников пикника '))
hotdog=int(input('Введите количество хотдогов для каждого '))

packing_of_sausages2=hotdog*person%10
packing_of_sausages3=hotdog*person//10
if packing_of_sausages2>0:
    packing_of_sausages3=packing_of_sausages3+1
    print('нужно упаковок сосисок',packing_of_sausages3)
else:
    print('нужно упаковок сосисок',packing_of_sausages3)
   
packing_of_buns2=hotdog*person%8
packing_of_buns3=hotdog*person//8

if packing_of_buns2>0:
    packing_of_buns3=packing_of_buns3+1
    print('нужно упаковок булочек',packing_of_buns3)
else:
    print('нужно упаковок булочек',packing_of_buns3)
    
the_rest_of_the_sausages=packing_of_sausages3*10-hotdog*person
the_rest_of_the_buns=packing_of_buns3*8-hotdog*person
print('осталось сосисок',the_rest_of_the_sausages)
print('осталось булочек',the_rest_of_the_buns)
