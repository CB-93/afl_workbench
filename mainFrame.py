from tkinter import * #todo have specific list of tkinter modules to import
from modules.workbench.listingPanel import *
from modules.workbench.interpreterPanel import *
from modules.output.outputFrame import *

class mainFrame:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1500x600")
        self.root.wm_title("AFL Workbench")
        self.root.config(background="#FFFFFF")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.leftFrame = Frame(self.root, width=400, height=600)
        self.leftFrame.grid(row=0, column=0, padx=0, pady=2, rowspan=2)

        self.rightFrame = Frame(self.root, width=500, height=300)
        self.rightFrame.grid(row=0, column=1, padx=10, pady=2, sticky="N")

        self.bottomFrame = Frame(self.root, width=500, height=300)
        self.bottomFrame.grid(row=1, column=1, padx=10, pady=2)

        self.leftPanel = listingPanel(self.root, self.leftFrame)
        self.rightPanel = interpreterPanel(self.root, self.rightFrame)
        self.bottomPanel = outputFrame(self.root, self.bottomFrame)

        # trying out using mainFrame to pass inputs across elements
        # with event bindings

        # binding for mac os only
        '''
        todo add non-mac bindings, but detect current working OS
        and keep modular
        '''
        self.keyboardBindingsExecute = [
            '<Meta_L><Shift_L><Return>',
            '<Control_L><Shift_L><Return>']
        for c in self.keyboardBindingsExecute:
            self.root.bind(
                c,
                lambda event, arg=self.rightPanel.aflText: self.rightPanel.onExecute(event, self.bottomPanel)
            )
    def start(self):
        self.root.mainloop()