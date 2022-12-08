number=int(input('Введите число '))

def is_prime(number):
    for number in range(2,number,1):
        total=0
        if number%a!=0:
           total=total+1
           if total==1:
              print('Число является простым')
           else:
              print('Число не является простым')
        else:
            print('Попробуйте еще раз')

is_prime(number)

