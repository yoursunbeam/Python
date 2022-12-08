def main():
    text=input('Введите текст без пробелов,но все слова начинаются с заглавной буквы ')
    #разбить текст на буквы
    new=list(text)
  
    total=[]
    #добавить пробел перед заглавными буквами
    #преобразовать заглавные буквы в строчные
    for i in new:
        if i.isupper():
            i=' '+i.lower()
            total.append(i)
        else:
            i=i
            total.append(i)
    #Получить первый символ        
    a=total[0]


    #преобразовать в текст
    new2=''
    
    for i in total:
        new2=new2+i
    
    
    #удалить первую букву предложения
    new3=new2.lstrip(a)
    
    

    #преобразовать первую букву предложения в заглавную и добавить к тексту
    
    new4=a.upper()+new3
    print(new4)

main()
        
    
