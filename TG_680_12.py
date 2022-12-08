import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=600,height=400)

        
        self.canvas.create_oval(10,150,110,250,fill='orangered')
        self.canvas.create_text(60,260,text='Солнце')
        
        self.canvas.create_oval(120,190,140,210,fill='grey')
        self.canvas.create_text(135,230,text='Меркурий')
        
        self.canvas.create_oval(150,185,180,215,fill='yellow')
        self.canvas.create_text(170,170,text='Венера')
        
        self.canvas.create_oval(190,190,210,210,fill='cyan')
        self.canvas.create_text(200,220,text='Земля')
        
        self.canvas.create_oval(220,190,240,210,fill='red')
        self.canvas.create_text(230,180,text='Марс')

        self.canvas.create_oval(250,160,330,240,fill='peachpuff')
        self.canvas.create_text(290,250,text='Юпитер')

        self.canvas.create_oval(340,180,440,220)
        self.canvas.create_oval(360,170,420,230,fill='lightyellow')
        self.canvas.create_text(390,160,text='Сатурн')

        self.canvas.create_oval(450,175,500,225,fill='deepskyblue')
        self.canvas.create_text(480,240,text='Уран')

        self.canvas.create_oval(510,180,550,220,fill='blue')
        self.canvas.create_text(530,160,text='Нептун')

        self.canvas.create_oval(560,190,580,210,fill='burlywood')
        self.canvas.create_text(570,220,text='Плутон')



        

        
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
