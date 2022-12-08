def main():
    
    infile_boys=open('BoysNames.txt','r')
    names_boys=infile_boys.readlines()
    infile_girls=open('GirlsNames.txt','r')
    names_girls=infile_girls.readlines()
    
    infile_boys.close()
    infile_girls.close()
    
    index=0
    while index<len(names_boys):
        names_boys[index]=names_boys[index].rstrip('\n')
        index=index+1
        
    index=0
    while index<len(names_girls):
        names_girls[index]=names_girls[index].rstrip('\n')
        index=index+1

    name=input('Введите имя ')
        
    again='d'
    while again=='d':       
        if name in names_boys:
            print(name,'есть в списке популярных')
        elif name in names_girls:
            print(name,'есть в списке популярных')
        else:
            print(name,'нет в списке популярных')
        
        again=input('Если хотите сыграть еще раз,нажмите d ')
        if again=='d':
            name=input('Введите имя ')
        else:
            print('goodbye')
    
main()
