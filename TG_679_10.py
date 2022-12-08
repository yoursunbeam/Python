import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=600,height=400)

        self.canvas.create_line(176,237,250,10)
        self.canvas.create_line(250,10,323,237)
        self.canvas.create_line(323,237,130,97)
        self.canvas.create_line(130,97,370,97)
        self.canvas.create_line(370,97,176,237)

        self.canvas.create_text(250,130,text='Kate')
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
