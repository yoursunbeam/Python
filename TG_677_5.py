import tkinter


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.value1=tkinter.StringVar()
        self.value2=tkinter.StringVar()
        

        self.frame1=tkinter.Frame(self.main_window)

        self.frame2=tkinter.Frame(self.main_window)

        self.frame3=tkinter.Frame(self.main_window)

        self.frame4=tkinter.Frame(self.main_window)
        

        self.label1=tkinter.Label(self.frame1,text='Введите стоимость имущества')

        self.label2=tkinter.Label(self.frame2,text='Оценочная стоимость')

        self.label3=tkinter.Label(self.frame3,text='Налог на имущество')

        self.label4=tkinter.Label(self.frame2,textvariable=self.value1)
        
        self.label5=tkinter.Label(self.frame3,textvariable=self.value2)
        

        self.entry=tkinter.Entry(self.frame1,width=10)
        

        self.my_button1=tkinter.Button(self.frame4,
                                      text='Вычислить',
                                      command=self.do_something)
        self.my_button2=tkinter.Button(self.frame4,
                                      text='Выйти',
                                      command=self.main_window.destroy)
    
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        
        
        self.entry.pack(side='left')
        
        
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        
        tkinter.mainloop()

    def do_something(self):

        property_value=float(self.entry.get())
        estimated_cost=property_value*0.6
        property_tax=estimated_cost*0.0075
        
        self.value1.set(estimated_cost)
        self.value2.set(property_tax)
        
        
my_gui=MyGUI()


        
    
        
