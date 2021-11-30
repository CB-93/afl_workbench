from tkinter import Button, Frame, Toplevel
from mainFrame import *

class loginFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.loginButton = Button(
            text = "Open",
            command = lambda : self.open_login()
        )
        self.loginButton.grid()

    def open_login(self):
        self.master.destroy()
        self.app = mainFrame()
        self.master.mainloop()
