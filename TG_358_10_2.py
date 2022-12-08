def read():
    file=open('golf.txt','r')
    name=file.readline()
    while name!='':
        score=file.readline()

        name=name.rstrip('\n')
        score=score.rstrip('\n')

        print(name,':',score)
        print()

        name=file.readline()
    file.close()
read()
