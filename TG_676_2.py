import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.top_frame=tkinter.Frame(self.main_window)

        self.bottom_frame=tkinter.Frame(self.main_window)

        self.value=tkinter.StringVar()

        self.label=tkinter.Label(self.top_frame,textvariable=self.value)

        self.my_button1=tkinter.Button(self.bottom_frame,
                                      text='sinister',
                                      command=self.do_left)
        self.my_button2=tkinter.Button(self.bottom_frame,
                                      text='dexter',
                                      command=self.do_right)
        self.my_button3=tkinter.Button(self.bottom_frame,
                                      text='medium',
                                      command=self.do_central)
    
        self.label.pack()
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='left')
        self.my_button3.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()

    def do_left(self):

        translate='левый'
        self.value.set(translate)
        
    def do_right(self):

        translate='правый'
        self.value.set(translate)
       
    def do_central(self):

        translate='центральный'
        self.value.set(translate)
        

        
my_gui=MyGUI()


        
    
        
