def main():
    file=input('Введите имя файла ')
    infile=open(file,'r')
    line=infile.readline()
    total=0
          
    for line in infile:
        line=infile.readline()
        line=line.rstrip('\n')
        total=total+1
        print(total,':',line)
        
    infile.close()
    
main()
