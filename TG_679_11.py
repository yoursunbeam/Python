import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=600,height=500)

        self.canvas.create_rectangle(250,50,550,250,fill='red')
        self.canvas.create_rectangle(150,150,250,250,fill='cyan')
        self.canvas.create_oval(180,230,220,270,fill='black')
        self.canvas.create_oval(480,230,520,270,fill='black')
        
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
