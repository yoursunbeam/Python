import tkinter


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.value1=tkinter.StringVar()
        self.value2=tkinter.StringVar()
        self.value3=tkinter.StringVar()
        

        self.top_frame=tkinter.Frame(self.main_window)

        self.bottom_frame=tkinter.Frame(self.main_window)

        self.label1=tkinter.Label(self.top_frame,textvariable=self.value1)

        self.label2=tkinter.Label(self.top_frame,textvariable=self.value2)

        self.label3=tkinter.Label(self.top_frame,textvariable=self.value3)

        self.my_button1=tkinter.Button(self.bottom_frame,
                                      text='Показать инфо',
                                      command=self.do_something)
        self.my_button2=tkinter.Button(self.bottom_frame,
                                      text='Выйти',
                                      command=self.main_window.destroy)
    
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()

    def do_something(self):
        
        translate1='394029, РФ, Воронежская область,'
        translate2='г.Воронеж,ул.Героев Стратосферы,д.14 кв.36'
        translate3='Лагутина Екатерина Станиславовна'
        self.value1.set(translate1)
        self.value2.set(translate2)
        self.value3.set(translate3)
        

        
my_gui=MyGUI()


        
    
        
