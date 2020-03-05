from Action import Action
from SubjectLabel import SubjectLabel
import os
import tkinter.messagebox as msg

class Load(Action):

    def __init__(self , master , subjList):
        super().__init__()
        self.butt.config(text = "Load")
        self.master = master
        self.subjList = subjList
        self.wind.bind("<Return>",self.execute)
        

    def execute(self,event= None):
        Action.execute(self)

        f = open(os.path.expanduser(self.filename),"r")
        L = f.readlines()

        for line in L:
            temp = line.split("\t")
            lecText = temp[1]
            temp[2] = temp[2].replace("\n","")
            tutText = None if(temp[2] == "None") else temp[2]
            
            tempSub = SubjectLabel(self.master , lecText , tutText)
            if(tempSub) not in self.subjList:
                self.subjList.append(tempSub)
                tempSub.SubLabel.bind("<Button-1>",self.remove_subject)
                tempSub.SubLabel.pack()


        f.close()
        self.wind.destroy()
    
    def remove_subject(self,event):
        subj = event.widget
        if msg.askyesno("Really Delete?", "Delete " + subj.cget("text") + "?"):
            for subj in self.subjList:
                if(subj.SubLabel == event.widget):
                    self.subjList.remove(subj)
                    event.widget.destroy()

