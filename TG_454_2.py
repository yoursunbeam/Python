mystring='Happy Birthday,Kate!'
total=0
for ch in mystring:
    if ch.isspace():
        total=total+1
print('Количество пробелов',total)
        
