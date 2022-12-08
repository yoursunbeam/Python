room={'CS101':3004,'CS102':4501,'CS103':6755,'CS104':1244,'CS105':1411}
teacher={'CS101':'Хайнц','CS102':'Альварадо','CS103':'Рич','NT110':'Берк','CM241':'Ли'}
time={'CS101':'8:00','CS102':'9:00','CS103':'10:00','NT110':'11:00','CM241':'13:00'}
course=input('Введите название курса ')
room1=room.get(course,'Номер аудитории не известен')
teacher1=teacher.get(course,'Преподаватель не известен')
time1=time.get(course,'Время не известно')
print(course,room1,teacher1,time1)
