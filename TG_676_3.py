import tkinter


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.value=tkinter.StringVar()
        

        self.frame1=tkinter.Frame(self.main_window)

        self.frame2=tkinter.Frame(self.main_window)

        self.frame3=tkinter.Frame(self.main_window)

        self.frame4=tkinter.Frame(self.main_window)
        

        self.label1=tkinter.Label(self.frame1,text='Введите количество галлонов')

        self.label2=tkinter.Label(self.frame2,text='Введите количество миль')

        self.label3=tkinter.Label(self.frame3,text='Мили на галлон (MPG)')

        self.label4=tkinter.Label(self.frame3,textvariable=self.value)
        

        self.entry1=tkinter.Entry(self.frame1,width=10)

        self.entry2=tkinter.Entry(self.frame2,width=10)
        

        self.my_button1=tkinter.Button(self.frame4,
                                      text='Вычислить MPG',
                                      command=self.do_something)
        self.my_button2=tkinter.Button(self.frame4,
                                      text='Выйти',
                                      command=self.main_window.destroy)
    
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        self.label4.pack(side='left')
        
        self.entry1.pack(side='left')
        self.entry2.pack(side='left')
        
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        
        tkinter.mainloop()

    def do_something(self):

        gallons=float(self.entry1.get())
        miles=float(self.entry2.get())
        mpg=miles/gallons
        
        self.value.set(mpg)
        
        
my_gui=MyGUI()


        
    
        
