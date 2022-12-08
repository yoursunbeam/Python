
total_amount=0
package=int(input('Введите количество приобретенных программмных пакетов '))
if package>=10 and package<=19:
    print('Скидка 10%')
    total_amount=99*package-99*package*0.1
    print('общая сумма покупок',total_amount,'$')
elif package>=20 and package<=49:
    print('Скидка 20%')
    total_amount=99*package-99*package*0.2
    print('общая сумма покупок',total_amount,'$')
elif package>=50 and package<=99:
    print('Скидка 30%')
    total_amount=99*package-99*package*0.3
    print('общая сумма покупок',total_amount,'$')
elif package>=100:
    total_amount=99*package-99*package*0.4
    print('общая сумма покупок',total_amount,'$')
    print('Скидка 40%')
else:
    print('Скидка 0%')
    total_amount=99*package
    print('общая сумма покупок',total_amount,'$')
    
