from Action import Action
from SubjectLabel import SubjectLabel
import os
import tkinter.messagebox as msg
from Error import Error

class Load(Action):

    def __init__(self , master , subjList):
        super().__init__()
        self.butt.config(text = "Load")
        self.master = master
        self.subjList = subjList
        self.wind.bind("<Return>",self.execute)
        

    def execute(self,event= None):
        Action.execute(self)
        #check if the filename has 
        if(len(self.filename)==0):
            _ = Error("File must have a name")
            return

        self.filename = self.filename.split(",")
        for flname in self.filename :
            
            fullfilename = os.getcwd() + '/' +flname.strip() +'.txt'

            if (os.path.isfile(fullfilename)):
                self.load_from_file(fullfilename)

            else:
                _ = Error("File " + flname + " Not Found")
                continue
        self.filename = ""
        self.wind.destroy()
    
    def remove_subject(self,event):
        subj = event.widget
        if msg.askyesno("Really Delete?", "Delete " + subj.cget("text") + "?"):
            for subj in self.subjList:
                if(subj.SubLabel == event.widget):
                    self.subjList.remove(subj)
                    event.widget.destroy()

    def load_from_file(self,filename):

        f = open(os.path.expanduser(filename),"r")
        L = f.readlines()

        for line in L:
            temp = line.split("\t")
            lecText = temp[1]
            temp[2] = temp[2].replace("\n","")
            tutText = None if(temp[2] == "None") else temp[2]
            
            tempSub = SubjectLabel(self.master , lecText , tutText)
            isDuplicate = False
            for subjCheck in self.subjList:
                if(subjCheck.SubObj == tempSub.SubObj):
                    isDuplicate = True
            if not (isDuplicate):
                self.subjList.append(tempSub)
                tempSub.SubLabel.bind("<Button-1>",self.remove_subject)
                tempSub.SubLabel.pack()


        f.close()

        

