
weight=int(input('Введите массу пакета '))
if weight<=200:
    print('оплатите 150руб')
elif weight>200 and weight<=600:
    print('оплатите 300руб')
elif weight>600 and weight<=1000:
    print('оплатите 400руб')
else:
    print('оплатите 475руб')
