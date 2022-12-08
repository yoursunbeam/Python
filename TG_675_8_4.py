import tkinter


class MyGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.canvas=tkinter.Canvas(self.main_window,
                                   width=200,height=200)
        self.canvas.create_arc(20,20,180,180,start=0, extent=90,fill='blue')
        
        self.canvas.pack()

        tkinter.mainloop()

data=MyGUI()
