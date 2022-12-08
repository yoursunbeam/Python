def main():
    infile=open('numbers.txt','r')
    line=infile.readline()
    total=0
    while line!='':
        amount=int(line)
        total=amount+total
        line=infile.readline()
    print(total)
          
    infile.close()
    
main()
