import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        

        self.frame1=tkinter.Frame(self.main_window)
        self.frame2=tkinter.Frame(self.main_window)
        self.frame3=tkinter.Frame(self.main_window)

        self.radio_var=tkinter.IntVar()
        
        self.radio_var.set(1)

        self.rb1=tkinter.Radiobutton(self.frame1,
                                     text='Дневное время (6:00-17:59)',
                                     variable=self.radio_var,
                                     value=10)
        self.rb2=tkinter.Radiobutton(self.frame1,
                                     text='Вечернее время (18:00-23:59)',
                                     variable=self.radio_var,
                                     value=12)
        self.rb3=tkinter.Radiobutton(self.frame1,
                                     text='Непиковый период (00:00-5:59)',
                                     variable=self.radio_var,
                                     value=5)
        
        self.label=tkinter.Label(self.frame2,text='Введите количество минут')

        self.entry=tkinter.Entry(self.frame2,width=10)
        

        self.my_button1=tkinter.Button(self.frame3,
                                      text='Показать стоимость',
                                      command=self.do_something)
        self.my_button2=tkinter.Button(self.frame3,
                                      text='Выйти',
                                      command=self.main_window.destroy)
    
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.label.pack(side='left')
        self.entry.pack(side='left')
        
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
    
        
        tkinter.mainloop()

    def do_something(self):

        minutes=int(self.entry.get())

        rate=self.radio_var.get()
        
        cost=minutes*rate
        
        tkinter.messagebox.showinfo('Общая стоимость',str(cost))
        
            
        
        
my_gui=MyGUI()


        
    
        
