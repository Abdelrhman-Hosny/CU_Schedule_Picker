import tkinter as tk


class Error:
    def __init__(self,ErrorMsg):
        self.wind = tk.Toplevel()
        self.wind.title("Error")
        self.lbl = tk.Label(self.wind , text = ErrorMsg ,padx= 10 ,  pady=10)
        self.lbl.pack(side=tk.TOP)
        self.butt = tk.Button(self.wind,text = "Ok",command = self.wind.destroy)
        self.butt.pack(side = tk.BOTTOM)
