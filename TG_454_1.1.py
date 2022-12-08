def main():
    last_name=input('Введите вашу фамилию ')
    first_name=input('Введите ваше имя ')
    patronymic=input('Введите вашу отчество ')
    set1=last_name[0]
    set2=first_name[0]
    set3=patronymic[0]
    initials=set1+'.'+set2+'.'+set3+'.'
    print(initials)

main()
