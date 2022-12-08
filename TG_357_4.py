def main():
    infile=open('names.txt','r')
    line=infile.readline()
    total=0
          
    for line in infile:
        line=infile.readline()
        total=total+1
    print(total)
        
    infile.close()
    
main()
