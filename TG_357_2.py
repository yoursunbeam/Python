def main():
    file=input('Введите имя файла ')
    infile=open(file,'r')
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    line4=infile.readline()
    line5=infile.readline()

    line1=line1.rstrip('\n')
    line2=line2.rstrip('\n')
    line3=line3.rstrip('\n')
    line4=line4.rstrip('\n')
    line5=line5.rstrip('\n')
    
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
main()
