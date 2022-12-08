def main():
    infile=open('number_list.txt','r')
    line=infile.readline()
    total=0
    while line !='':
        x=int(line)
        total=total+x
        line=infile.readline()
    print(total)
    infile.close()

main()
