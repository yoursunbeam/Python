dct={'а':1,'б':2,'в':3,'Джим':20}
if 'Джим' in dct:
    del dct['Джим']
    print('Успешно удалено')
    print(dct)
else:
    print('Такой ключ не найден')
