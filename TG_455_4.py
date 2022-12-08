def main():
    cod=input('введите фразу для перевода заглавными буквами ')
    morse=[]
    for i in cod:
        if i==' ':
            letter=' '
            morse.append(letter)
        elif i==',':
            letter='-..-'
            morse.append(letter)
        elif i=='.':
            letter='.-.-.-'
            morse.append(letter)
        elif i=='?':
            letter='..--..'
            morse.append(letter)
        elif i=='0':
            letter='-----'
            morse.append(letter)
        elif i=='1':
            letter='.----'
            morse.append(letter)
        elif i=='2':
            letter='..---'
            morse.append(letter)
        elif i=='3':
            letter='...--'
            morse.append(letter)
        elif i=='4':
            letter='....-'
            morse.append(letter)
        elif i=='5':
            letter='.....'
            morse.append(letter)
        elif i=='6':
            letter='-....'
            morse.append(letter)
        elif i=='7':
            letter='--...'
            morse.append(letter)
        elif i=='8':
            letter='---..'
            morse.append(letter)
        elif i=='9':
            letter='----.'
            morse.append(letter)
        elif i=='A':
            letter='.-'
            morse.append(letter)
        elif i=='B':
            letter='-...'
            morse.append(letter)
        elif i=='C':
            letter='-.-.'
            morse.append(letter)
        elif i=='D':
            letter='-..'
            morse.append(letter)
        elif i=='E':
            letter='.'
            morse.append(letter)
        elif i=='F':
            letter='..-.'
            morse.append(letter)
        elif i=='G':
            letter='--.'
            morse.append(letter)
        elif i=='H':
            letter='....'
            morse.append(letter)
        elif i=='I':
            letter='..'
            morse.append(letter)
        elif i=='J':
            letter='.---'
            morse.append(letter)
        elif i=='K':
            letter='-.-'
            morse.append(letter)
        elif i=='L':
            letter='.-..'
            morse.append(letter)
        elif i=='M':
            letter='--'
            morse.append(letter)
        elif i=='N':
            letter='-.'
            morse.append(letter)
        elif i=='O':
            letter='---'
            morse.append(letter)
        elif i=='P':
            letter='.--.'
            morse.append(letter)
        elif i=='Q':
            letter='--.-'
            morse.append(letter)
        elif i=='R':
            letter='.-.'
            morse.append(letter)
        elif i=='S':
            letter='...'
            morse.append(letter)
        elif i=='T':
            letter='-'
            morse.append(letter)
        elif i=='U':
            letter='..-'
            morse.append(letter)
        elif i=='V':
            letter='...-'
            morse.append(letter)
        elif i=='W':
            letter='.--'
            morse.append(letter)
        elif i=='X':
            letter='-..-'
            morse.append(letter)
        elif i=='Y':
            letter='-.-'
            morse.append(letter)
        elif i=='Z':
            letter='--..'
            morse.append(letter)
        elif i=='А':
            letter='.-'
            morse.append(letter)
        elif i=='Б':
            letter='-...'
            morse.append(letter)
        elif i=='В':
            letter='.--'
            morse.append(letter)
        elif i=='Г':
            letter='--.'
            morse.append(letter)
        elif i=='Д':
            letter='-..'
            morse.append(letter)
        elif i=='Е'or i=='Ё':
            letter='.'
            morse.append(letter)
        elif i=='Ж':
            letter='...-'
            morse.append(letter)
        elif i=='З':
            letter='--..'
            morse.append(letter)
        elif i=='И':
            letter='..'
            morse.append(letter)
        elif i=='Й':
            letter='.---'
            morse.append(letter)
        elif i=='К':
            letter='-.-'
            morse.append(letter)
        elif i=='Л':
            letter='.-..'
            morse.append(letter)
        elif i=='М':
            letter='--'
            morse.append(letter)
        elif i=='Н':
            letter='-.'
            morse.append(letter)
        elif i=='О':
            letter='---'
            morse.append(letter)
        elif i=='П':
            letter='.--.'
            morse.append(letter)
        elif i=='Р':
            letter='.-.'
            morse.append(letter)
        elif i=='С':
            letter='...'
            morse.append(letter)
        elif i=='Т':
            letter='-'
            morse.append(letter)
        elif i=='У':
            letter='..-'
            morse.append(letter)
        elif i=='Ф':
            letter='..-.'
            morse.append(letter)
        elif i=='Х':
            letter='....'
            morse.append(letter)
        elif i=='Ц':
            letter='-.-.'
            morse.append(letter)
        elif i=='Ч':
            letter='---.'
            morse.append(letter)
        elif i=='Ш':
            letter='----'
            morse.append(letter)
        elif i=='Щ':
            letter='--.-'
            morse.append(letter)
        elif i=='Ъ':
            letter='.--.-.'
            morse.append(letter)
        elif i=='Ы':
            letter='-.--'
            morse.append(letter)
        elif i=='Ь':
            letter='-..-'
            morse.append(letter)
        elif i=='Э':
            letter='..-..'
            morse.append(letter)
        elif i=='Ю':
            letter='..--'
            morse.append(letter)
        elif i=='Я':
            letter='.-.-'
            morse.append(letter)
        else:
            print('error')

    

    index=0
    morse_new=''
    while index<len(morse):
        num=morse[index]
        morse_new=morse_new+num
        index=index+1
            
    print(morse_new)

    
main()
        
