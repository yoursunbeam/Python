import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=600,height=400)

        self.canvas.create_oval(10,30,590,350,outline='blue')
        self.canvas.create_text(555,190,text='5 years')
        

        self.canvas.create_oval(20,60,520,320,outline='green')
        self.canvas.create_text(485,190,text='4 years')

        self.canvas.create_oval(30,100,450,290,outline='yellow')
        self.canvas.create_text(415,190,text='3 years')

        self.canvas.create_oval(40,130,380,260,outline='orange')
        self.canvas.create_text(345,190,text='2 years')

        self.canvas.create_oval(50,160,310,230,outline='red')
        self.canvas.create_text(275,190,text='1 years')
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
