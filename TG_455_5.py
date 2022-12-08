def main():
    word=input('Введите номер телефона в формате XXX-XXX-XXXX ')
    number=[]
    for i in word:
        if i=='-':
            letter='-'
            number.append(letter)
        elif i=='A' or i=='B' or i=='C' or i=='2':
            letter='2'
            number.append(letter)
        elif i=='D' or i=='E' or i=='F'or i=='3':
            letter='3'
            number.append(letter)
        elif i=='G' or i=='H' or i=='I'or i=='4':
            letter='4'
            number.append(letter)
        elif i=='J' or i=='K' or i=='L'or i=='5':
            letter='5'
            number.append(letter)
        elif i=='M' or i=='N' or i=='O'or i=='6':
            letter='6'
            number.append(letter)
        elif i=='P' or i=='Q' or i=='R' or i=='S'or i=='7':
            letter='7'
            number.append(letter)
        elif i=='T' or i=='U' or i=='V'or i=='8':
            letter='8'
            number.append(letter)
        elif i=='W' or i=='X' or i=='Y' or i=='Z'or i=='9':
            letter='9'
            number.append(letter)
        elif i=='1':
            letter='1'
            number.append(letter)
        else:
            print(error)

    index=0
    number_new=''
    while index<len(number):
        num=number[index]
        number_new=number_new+num
        index=index+1
            
    print(number_new)

    
main()
            
            
            
            
    
