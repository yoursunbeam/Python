def main():
    infile=open('number_list.txt','r')
    line=infile.readline()
    while line !='':
        x=int(line)
        print(x)
        line=infile.readline()
    infile.close()

main()
        
