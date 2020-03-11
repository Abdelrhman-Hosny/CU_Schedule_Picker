import tkinter as tk



class Tips:

    def __init__(self):

        self.root = tk.Toplevel()
        self.lbl1 = tk.Label(self.root , text = "Times must be in 24-Hour format for program to work", pady = 10 , padx = 10)
        self.lbl2 = tk.Label(self.root , text = "Fill information for each subject individually and then load them all at once", pady = 10 , padx = 10)
        self.lbl3 = tk.Label(self.root , text = "You can load multiple files by clicking load and then\n in the windows type 'File1Name , File2Name ..etc", pady = 10 , padx = 10)
        self.lbl1.pack()
        self.lbl2.pack()
        self.lbl3.pack()
        