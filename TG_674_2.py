import tkinter

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.label1=tkinter.Label(self.main_window,text='Программировать-это круто!')
        self.label2=tkinter.Label(self.main_window,text='Ура!')
        
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        
        tkinter.mainloop()

my_gui=MyGUI()
