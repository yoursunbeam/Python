import random
even=0
uneven=0
for count in range(100):
    number=random.randint(1,100)
    if (number%2)==0:
        even=even+1
    else:
        uneven=uneven+1
print('Количество четных=',even)
print('Количество нечетных=',uneven)
