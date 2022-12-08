import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        

        self.frame1=tkinter.Frame(self.main_window)

        self.frame2=tkinter.Frame(self.main_window)

        self.cb_var1=tkinter.IntVar()
        self.cb_var2=tkinter.IntVar()
        self.cb_var3=tkinter.IntVar()
        self.cb_var4=tkinter.IntVar()
        self.cb_var5=tkinter.IntVar()
        self.cb_var6=tkinter.IntVar()
        self.cb_var7=tkinter.IntVar()
        

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        
        self.cb1=tkinter.Checkbutton(self.frame1,text='Замена масла-500.00',variable=self.cb_var1)

        self.cb2=tkinter.Checkbutton(self.frame1,text='Смазочные работы-300.00',variable=self.cb_var2)

        self.cb3=tkinter.Checkbutton(self.frame1,text='Промывка радиатора-700.00',variable=self.cb_var3)

        self.cb4=tkinter.Checkbutton(self.frame1,text='Замена жидкости в трансмиссии-1000.00',variable=self.cb_var4)

        self.cb5=tkinter.Checkbutton(self.frame1,text='Осмотр-800.00',variable=self.cb_var5)

        self.cb6=tkinter.Checkbutton(self.frame1,text='Ремонт глушителя-1300.00',variable=self.cb_var6)

        self.cb7=tkinter.Checkbutton(self.frame1,text='Шиномонтаж-1300.00',variable=self.cb_var7)
        

        self.my_button1=tkinter.Button(self.frame2,
                                      text='Показать стоимость',
                                      command=self.do_something)
        self.my_button2=tkinter.Button(self.frame2,
                                      text='Выйти',
                                      command=self.main_window.destroy)
    
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        
        
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        
        self.frame1.pack()
        self.frame2.pack()
    
        
        tkinter.mainloop()

    def do_something(self):

        cost1=0
        cost2=0
        cost3=0
        cost4=0
        cost5=0
        cost6=0
        cost7=0

        if self.cb_var1.get()==1:
            cost1=500.00
        if self.cb_var2.get()==1:
            cost2=300.00
        if self.cb_var3.get()==1:
            cost3=700.00
        if self.cb_var4.get()==1:
            cost4=1000.00
        if self.cb_var5.get()==1:
            cost5=800.00
        if self.cb_var6.get()==1:
            cost6=1300.00
        if self.cb_var7.get()==1:
            cost7=1300.00

        total=cost1+cost2+cost3+cost4+cost5+cost6+cost7
        
        tkinter.messagebox.showinfo('Общая стоимость',str(total))
        
            
        
        
my_gui=MyGUI()


        
    
        
