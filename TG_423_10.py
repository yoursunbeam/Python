def main():
    
    infile=open('WorldSeriesWinners.txt','r')
    winners=infile.readlines()
    
    infile.close()

    search=input('Введите название команды ')

    
    index=0
    while index<len(winners):
        winners[index]=winners[index].rstrip('\n')
        index=index+1

    index=0
    print(winners)

    
    for n in range(len(winners)):
        if n==search:
           index=index+1
    print(search,'побеждала',index,'лет')
    

    
    

       
    
main()

