#Напишите программу с GUI, которая преобразует
#показания температуры по шкале Цельсия в температуру по шкале Фаренгейта.
#Пользователь должен иметь возможность вводить температуру по шкале Цельсия, нажимать
#кнопку и затем получать эквивалентную температуру по шкале Фаренгейта


import tkinter


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.value=tkinter.StringVar()
        

        self.frame1=tkinter.Frame(self.main_window)

        self.frame2=tkinter.Frame(self.main_window)

        self.frame3=tkinter.Frame(self.main_window)
        

        self.label1=tkinter.Label(self.frame1,text='Введите температуру в градусах Цельсия')

        self.label2=tkinter.Label(self.frame2,text='Температура по шкале Фаренгейта')

        self.label3=tkinter.Label(self.frame2,textvariable=self.value)
        

        self.entry1=tkinter.Entry(self.frame1,width=10)
        

        self.my_button1=tkinter.Button(self.frame3,
                                      text='Преобразовать в градусы Фаренгейта',
                                      command=self.do_something)
        self.my_button2=tkinter.Button(self.frame3,
                                      text='Выйти',
                                      command=self.main_window.destroy)
    
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        
        self.entry1.pack(side='left')
        
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        
        tkinter.mainloop()

    def do_something(self):

        celsius=float(self.entry1.get())
        
        fahrenheit=1.8*celsius+32
        
        self.value.set(fahrenheit)
        
        
my_gui=MyGUI()


        
    
        
