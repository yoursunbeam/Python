def main():
    date=input('Введите дату в формате дд/мм/гггг ')
    date_new=date.split('/')
    
                             
    if date_new[1]=='01':
        date_new[1]='января'
    elif date_new[1]=='02':
        date_new[1]='февраля'
    elif date_new[1]=='03':
        date_new[1]='марта'
    elif date_new[1]=='04':
        date_new[1]='апреля'
    elif date_new[1]=='05':
        date_new[1]='мая'
    elif date_new[1]=='06':
        date_new[1]='июня'
    elif date_new[1]=='07':
        date_new[1]='июля'
    elif date_new[1]=='08':
        date_new[1]='августа'
    elif date_new[1]=='09':
        date_new[1]='сентября'
    elif date_new[1]=='10':
        date_new[1]='октября'
    elif date_new[1]=='11':
        date_new[1]='ноября'
    elif date_new[1]=='12':
        date_new[1]='декабря'
    else:
        print('ощибка,месяц должен быть от 01 до 12')
        
    date2=date_new[0]+' '+date_new[1]+' '+date_new[2]+'г.'
    print(date2)
main()
    
