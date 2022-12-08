def main():
    infile=open('text.txt','r')
    text=infile.readline()
    infile.close()

    index=0
    total=0
    while index<len(text):
        total=total+1
        index=index+1

    average=total/(len(text)+1)
    print('Среднее количество слов в предложении', average)

main()
    
