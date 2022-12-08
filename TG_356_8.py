import os
def create():
    found=False
    search=input('Оценку какого студента изменить? ')
    new_score=int(input('Введите оценку за экзамен '))
    st_file=open('students.txt','r')
    temp_file=open('temp.txt','w')
    descr=st_file.readline()
    while descr !='':
        score=st_file.readline()
        descr=descr.rstrip('\n')
        if descr==search:
            temp_file.write(descr+'\n')
            temp_file.write(str(new_score)+'\n')
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
    
        


    
        
