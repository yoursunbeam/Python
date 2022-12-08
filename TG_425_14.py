import matplotlib.pyplot as plt
def main():
    infile=open('expenses.txt','r')
    expenses=infile.readlines()
    infile.close()
    name_labels=['арендная плата','бензин','продукты питания','одежда','платежи по машине','прочие']
    index=0
    while index<len(expenses):
        expenses[index]=expenses[index].rstrip('\n')
        expenses[index]=int(expenses[index])
        index=index+1

    plt.pie(expenses,labels=name_labels)
    plt.show()

main()
