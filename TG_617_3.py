def main():
    n=int(input('Введите число '))
    traffic_sign(n)
    
def traffic_sign(n):
    if n>0:
        print('Не парковаться!')
        traffic_sign(n-1)
    else:
        print('Программа окончена')

main()
        
        
