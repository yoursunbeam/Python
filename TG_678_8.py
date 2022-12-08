import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=500,height=500)
        self.canvas.create_rectangle(100,250,400,450,fill='green')

        self.canvas.create_polygon(100,250,250,100,400,250,fill='brown',width=3)

        self.canvas.create_rectangle(215,320,285,440,fill='black')

        self.canvas.create_rectangle(120,320,180,400,fill='white')

        self.canvas.create_rectangle(320,320,380,400,fill='white')

        self.canvas.create_oval(400,20,450,70,fill='yellow')
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
