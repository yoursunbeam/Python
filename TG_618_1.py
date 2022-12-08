def main():
    num=1
    n=int(input('Введите число '))
    show_me(num,n)
    
def show_me(arg,n):
    print(arg)
    if arg<n:
        show_me(arg+1,n)
    
main()





        
        
