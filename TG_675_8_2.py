import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=200,height=200)
        self.canvas.create_rectangle(50,50,100,100,fill='black',outline='red')
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
