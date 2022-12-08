import random

def main():
    values=[]
            
    for i in range(1,8,1):
        i=random.randint(0,9)
        values.append(i)

    for i in values:
        print(i)
        
            
    
    
main()
