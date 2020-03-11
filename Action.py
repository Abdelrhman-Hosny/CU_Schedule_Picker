import tkinter as tk
import os


class Action:

    def __init__(self):

        self.wind = tk.Toplevel()
        self.lbl = tk.Label(self.wind,text="Enter Filename")
        self.butt = tk.Button(self.wind,text="temp",command = self.execute)
        self.entry = tk.Entry(self.wind,width=10)
        self.lbl.pack(side=tk.TOP)
        self.entry.pack(side=tk.TOP)
        self.butt.pack(side=tk.TOP)
        self.filename = ""

    def execute(self):
        self.filename = str(self.entry.get().strip())
        fullfilename = os.getcwd() + '/' +self.filename +'.txt'
        self.filename = fullfilename
        

