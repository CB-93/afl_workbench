from tkinter import *
# todo import specific modules

class interpreterPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        aflText = Text(self.root)
        aflText.grid(row=0, column=1, padx=10, pady=2)
        aflText.config(state="normal")