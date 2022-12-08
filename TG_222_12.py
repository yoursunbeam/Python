n=int(input('Введите неотрицательное целое число '))
factorial=1
for num in range (1,n+1,1):
    factorial=factorial*num
print('Факториал=',factorial)
