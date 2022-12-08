import tkinter
import tkinter.messagebox

class DataGUI:
    def __init__(self):

        self.main_window=tkinter.Tk()

        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        

        self.label=tkinter.Label(self.top_frame,
                                 text='Введите данные')
        self.data_entry=tkinter.Entry(self.top_frame,
                                 width=10)
        
        self.label.pack(side='left')
        self.data_entry.pack(side='left')


        self.my_button=tkinter.Button(self.bottom_frame,
                                      text='Нажми сюда',
                                      command=self.convert)
        self.my_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        var=int(self.data_entry.get())

        tkinter.messagebox.showinfo('Результаты',var)

data=DataGUI()
