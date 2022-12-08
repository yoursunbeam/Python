def main():
    infile=open('numbers.txt','r')
    line=infile.readline()
    total=0
    count=0
    while line!='':
        amount=int(line)
        total=amount+total
        count=count+1
        line=infile.readline()
    average=total/count
    print(average)
          
    infile.close()
    
main()
