import tkinter as tk



class Shortcuts:

    def __init__(self):

        self.root = tk.Toplevel()
        self.root.title("Shortcuts")
        self.lbl1 = tk.Label(self.root,text = "Ctrl + s : Save" , pady = 10 , padx = 10)
        self.lbl2 = tk.Label(self.root,text = "Ctrl + c : Clear", pady = 10 , padx = 10)
        self.lbl3 = tk.Label(self.root,text = "Ctrl + l : Load", pady = 10 , padx = 10)
        self.lbl1.pack()
        self.lbl2.pack()
        self.lbl3.pack()
        
