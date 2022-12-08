def main():
    text=input('Введите текст ')
    new=[]
    letters=0
    for i in text:
        if i.isalpha():
            letters=letters+1
    new.append(letters)
            
    figures=0
    for i in text:
        if i.isdigit():
            figures=figures+1
    new.append(figures)
            
    space=0
    for i in text:
        if i.isspace():
            space=space+1
    new.append(space)

    maximum=max(new)
    item=new.index(maximum)
    if item==0:
        print('Самый частый символ-буквы')
    elif item==1:
        print('Самый частый символ - цифры')
    else:
        print('Самый частый символ - пробел')

main()
    
