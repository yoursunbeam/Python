import random
jackpot=1000000
def main():
    
    values=[]
            
    for i in range(5):
        i=random.randint(1,69)
        values.append(i)
    i=random.randint(1,26)
    values.append(i)
    print(values)
    
    infile=open('pbnumbers.txt','r')
    numbers=infile.readlines()
    infile.close()
    
    while index<len(numbers):
        numbers[index]=numbers[index].rstrip('\n')
        numbers[index]=int(numbers[index])
        index=index+1
    for i in numbers:
        if values==i:
            

    
main()

