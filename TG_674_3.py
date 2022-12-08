import tkinter

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.frame=tkinter.Frame(self.main_window)
        
        self.label=tkinter.Label(self.frame,text='Программировать-это круто!')
        
        self.frame.pack()
        self.label.pack()
        
        
        tkinter.mainloop()

my_gui=MyGUI()
