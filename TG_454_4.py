mystring='Happy Birthday,Kate!34'
total=0
for ch in mystring:
    if ch.islower():
        total=total+1
print('Количество букв в нижнем регистре',total)
        
