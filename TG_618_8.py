def main():
    
    m=int(input('Введите небольшое значение '))
    n=int(input('Введите небольшое значение '))

    ack=ackermann(m,n)
    print(ack)
    
def ackermann(m,n):
    
    if m==0:
        return n+1
    elif n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))
            
main()

