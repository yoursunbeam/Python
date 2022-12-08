import random
state_capital={'Alabama':'Mongomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock',
        'California':'Los Angeles','Colorado':'Denver','Connecticut':'Hartford',
        'Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu',
         'Idaho':'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines',
        'Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta',
        'Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing Detroit',
        'Minnesota':'St. Paul','Mississippi':'Jackson','Missouri':'Jefferson City/Kansas City',
        'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City/Las Vegas',
        'New Hampshire':'Concord/ Manchester','New Jersey':'Trenton','New Mexico':'Santa Fe',
        'New York':'Albany/New York','North Carolina':'Raleigh','North Dakota':'Bismarck',
        'Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem/Portland',
        'Pennsylvania':'Harrisburg/Philadelphia','Rhode Island':'Providence',
        'South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':'Nashville/Memphis',
        'Texas':'Austin/Houston','Utah':'Salt Lake City','Vermont':'Montpelier',
        'Virginia':'Richmond','Washington':'Olympia/ Seattle','West Virginia':'Charleston',
        'Wisconsin':'Madison','Wyoming':'Cheyenne'}

state=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
        'Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
        'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
        'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire',
        'New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
        'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee',
        'Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

    

right=0
wrong=0
again='д'
while again.lower()=='д':
    
    num=random.randint(0,50)
    state_choice=state[num]
    print(state_choice)
    answer=input('Введите столицу штата ')
    capital=state_capital.get(state_choice,'Запись не найдена')
    
    
    
    if capital==answer:
        print('Вы выиграли!')
        right=right+1
        again=input('Хотите сыграть еще раз?д/н?')
        
    else:
        wrong=wrong+1
        print('Ошибка!')
        print('Правильный ответ',capital)
        again=input('Хотите сыграть еще раз?д/н?')

        
print('Правильных ответов',right)
print('Неправильных ответов',wrong)


