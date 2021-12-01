from tkinter import * #todo track modules used and only import those
from pandastable import Table, TableModel


class outputFrame:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.textName = "aflOutput"
        self.aflOutput = Text(self.root, width=200, name=self.textName)
        self.aflOutput.grid(row=1, column=1, padx=10, pady=2, sticky="N")
        self.aflOutput.config(state="normal")
    def inputExecute(self, command):
        print(command)