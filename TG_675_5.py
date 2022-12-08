import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.frame=tkinter.Frame(self.main_window)

        self.my_button=tkinter.Button(self.frame,
                                      text='Вычислить',
                                      command=self.calculate)
    
        self.frame.pack()
        self.my_button.pack()
        
        tkinter.mainloop()

    def calculate(self):
        tkinter.messagebox.showinfo('Вычисляем...',
                                'Нажмите Ok')

my_gui=MyGUI()
