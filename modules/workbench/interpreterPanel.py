from tkinter import END, Text
# todo import specific modules

class interpreterPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.aflText = Text(self.root, width=200)
        self.aflText.grid(row=0, column=1, padx=10, pady=2)
        self.aflText.config(state="normal")
        self.root.bind(
            '<Return>',
            lambda event, arg=self.aflText: self.onExecute(event)
        )
    def onExecute(self, event):
        print(self.aflText.get(1.0, END+"-1c"))
