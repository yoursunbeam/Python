def main():
    num=1
    f='*'
    n=int(input('Введите число '))
    show_me(num,n)
    
def show_me(arg,n):
   
   if arg<=n:
       print(arg*'*')
       return show_me(arg+1,n)
    
main()





        
        
