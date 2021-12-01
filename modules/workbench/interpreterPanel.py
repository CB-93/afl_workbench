from tkinter import END, IntVar, Text
import idlelib.colorizer as ic
import idlelib.percolator as ip
from ..output.outputFrame import *
# todo import specific modules

class interpreterPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.textName = "aflInterpreter"
        self.aflText = Text(self.root, width=200, name=self.textName)
        self.aflText.grid(row=0, column=1, padx=10, pady=2, sticky="N")
        self.aflText.config(state="normal")
        self.keywords = {
            "ADMIN": ["insert", "delete"],
            "DISPLAY": ["scan", "secure_scan", "list", "show"],
            "MODS": ["redimension", "apply"],
            "CREATE": ["create", "build"]
        }
        self.syntax_color_settings()
    def onExecute(self, event, displayFrame=None):
        # only if this window is focused on
        if str(self.root.focus_get()) == f".{self.textName}":
            myCommand = self.aflText.get(1.0, END+"-1c")
            displayFrame.inputExecute(myCommand)
        else:
            print("Focus on the interpreter window first")
            print(self.root.focus_get())
    def syntax_color_settings(self):
        syntax_compilation = "|".join([
            r"\b(?P<" + f"{k}" + f">{'|'.join(v)})" + r"\b"
            for k, v in self.keywords.items()])
        cdg = ic.ColorDelegator()
        cdg.prog = re.compile(syntax_compilation + "|" + ic.make_pat(), re.S)
        cdg.idprog = re.compile(r'\s+(\w+)', re.S)
        cdg.tagdefs['CREATE'] = {'foreground': '#7F7F7F',
                                 'background': '#FFFFFF'}
        cdg.tagdefs['ADMIN'] = {'foreground': '#7F7F7F',
                                'background': '#FFFFFF'}
        cdg.tagdefs['MODS'] = {'foreground': '#7F7F7F',
                               'background': '#FFFFFF'}
        cdg.tagdefs['DISPLAY'] = {'foreground': '#7F7F7F',
                                  'background': '#FFFFFF'}
        cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000',
                                  'background': '#FFFFFF'}
        cdg.tagdefs['KEYWORD'] = {'foreground': '#000000',
                                  'background': '#FFFFFF'}
        cdg.tagdefs['BUILTIN'] = {'foreground': '#000000',
                                  'background': '#FFFFFF'}
        cdg.tagdefs['STRING'] = {'foreground': '#7F3F00',
                                 'background': '#FFFFFF'}
        cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F',
                                     'background': '#FFFFFF'}
        ip.Percolator(self.aflText).insertfilter(cdg)