from tkinter import * #todo list specific modules to import
# todo import scidb for events


class listingPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        # contents
        Label(self.frame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)
        self.instruct = Label(self.frame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
        self.instruct.grid(row=1, column=0, padx=10, pady=2)