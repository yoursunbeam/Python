
def main():
    text=input('Введите текст ')
    vowels=0
    for i in text:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='Y' or i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='y':
            vowels=vowels+1
    print('Количество гласных',vowels)

    #общее количество букв
    total=0
    for i in text:
        if i.isalpha():
            total=total+1
    
   

    consonants=total-vowels
    print('Количество согласных',consonants)
main()
    
    

    
    
 
