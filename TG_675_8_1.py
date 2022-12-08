import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=200,height=200)
        self.canvas.create_line(0,0,199,199,fill='blue',width=3)
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
