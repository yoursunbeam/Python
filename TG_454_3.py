mystring='Happy Birthday,Kate!34'
total=0
for ch in mystring:
    if ch.isdigit():
        total=total+1
print('Количество цифр',total)
        
