mark1=int(input('Введите первую оценку '))
mark2=int(input('Введите вторую оценку '))
mark3=int(input('Введите третью оценку '))
mark4=int(input('Введите четвертую оценку '))
mark5=int(input('Введите пятую оценку '))

def calc_average(a,b,c,d,e):
    average=(a+b+c+d+e)/5
    return average

def determine_grade(score):
    if score >=90:
        print('A')
    elif (score>=80 and score<=89):
        print('B')
    elif (score>=70 and score<=79):
        print('C')
    elif (score>=60 and score<=69):
        print('D')
    else: 
        print('F')

average=calc_average(mark1,mark2,mark3,mark4,mark5)
print('Средний бал=',average)
determine_grade(average)

