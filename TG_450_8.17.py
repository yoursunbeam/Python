mystring='Happy Birthday,Kate!'
total=0
for ch in mystring:
    if ch.isupper():
        total=total+1
print('Количество букв в верхнем регистре',total)
        
