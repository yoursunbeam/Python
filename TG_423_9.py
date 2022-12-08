def main():
    
    infile=open('USPopulation.txt','r')
    population=infile.readlines()
    
    infile.close()
    
    index=0
    total=0
    summa=0
    average=[]

    years=[1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,
           1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]
    
    while index<len(population):
        population[index]=population[index].rstrip('\n')
        population[index]=int(population[index])
        index=index+1
        
        
    for n in range(1,len(population),1):
        increase=population[n]-population[n-1]
        average.append(increase)
    print(average)

    for n in average:
        summa=n+summa
    amount=summa/(len(average)+1)
    print('среднегодовое изменение численности',format(amount,'.2f'))

    max_increase=max(average)
    item_max=average.index(max_increase)
    print('год с наибольшим увеличением численности населения ',years[item_max])

    min_increase=min(average)
    item_min=average.index(min_increase)
    print('год с наименьшим увеличением численности населения ',years[item_min])
        

        
    
        
    
    
main()

