import matplotlib.pyplot as plt
def main():
    infile=open('price.txt','r')
    price=infile.readlines()
    infile.close()
    weeks=[1,2,3,4,5,6,7,8,9,10]
    index=0
    while index<len(price):
        price[index]=price[index].rstrip('\n')
        price[index]=int(price[index])
        index=index+1

    
    plt.plot(weeks,price,marker='o')

    plt.xlabel('weeks')
    plt.ylabel('price')

    plt.xticks([1,2,3,4,5,6,7,8,9,10],
               ['1','2','3','4','5','6','7','8','9','10'])
    
    
    plt.grid(True)
    plt.show()

main()
