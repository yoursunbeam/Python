books=int(input('Введите количество книг, приобретенных в этом месяце '))
if books==0:
    print('Вы заработали 0 очков')
elif books==2:
    print('Вы заработали 5 очков')
elif books==4:
    print('Вы заработали 15 очков')
elif books==6:
    print('Вы заработали 30 очков')
elif books>=8:
    print('Вы заработали 60 очков')
else:
    print('Чтобы получить баллы,нужно купить четное количество книг')
    
