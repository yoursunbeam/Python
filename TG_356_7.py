import os
def create():
    another='д'
    st_file=open('students.txt','w')
    while another=='д' or another=='Д':
        print('Введите данные о студенте')
        name=input('ФИ студента: ')
        score=int(input('Оценка за экзамен '))
        
        st_file.write(str(name)+'\n')
        st_file.write(str(score)+'\n')

        print('Желаете добавить еще одну запись?')
        another=input('д=да,все остальное - нет ')
    st_file.close()
    print('Данные добавлены в students.txt')
    
    found=False
    search=input('Какого студента удалить? ')
    st_file=open('students.txt','r')
    temp_file=open('temp.txt','w')
    descr=st_file.readline()
    
    while descr !='':
        name=st_file.readline()
        descr=descr.rstrip('\n')
        if descr!=search:
            temp_file.write(descr+'\n')
            temp_file.write(str(name)+'\n')
        else:
            found=True
        descr=st_file.readline()
    st_file.close()
    temp_file.close()
    os.remove('students.txt')
    os.rename('temp.txt','students.txt')

    if found:
        print('Файл обновлен')
    else:
        print('Фамилия не найдена')

create()
    
        


    
        
