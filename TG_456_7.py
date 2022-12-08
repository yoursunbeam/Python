def main():
    
    infile=open('text.txt','r')
    text=infile.readlines()
    infile.close()
    
    index=0
    while index<len(text):
        text[index]=text[index].rstrip('\n')
        index+=1
    
    text=str(text)
    
    total=0
    for ch in text:
        if ch.isspace():
            total=total+1
    print('Количество пробелов',total)
        
    total=0
    for ch in text:
        if ch.isdigit():
            total=total+1
    print('Количество цифр',total)
    total=0
    for ch in text:
        if ch.islower():
            total=total+1
    print('Количество букв в нижнем регистре',total)

    total=0
    for ch in text:
        if ch.isupper():
            total=total+1
    print('Количество букв в верхнем регистре',total)
        


main()
    


